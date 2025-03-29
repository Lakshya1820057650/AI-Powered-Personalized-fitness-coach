import cv2
import mediapipe as mp
import numpy as np
import pyttsx3

# Initialize Mediapipe Pose and Drawing
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Initialize Voice Engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust voice speed

# Function to calculate angle between three points
def calculate_angle(a, b, c):
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return 360 - angle if angle > 180 else angle

# Open Camera
cap = cv2.VideoCapture(0)
squat_position = None
voice_alert_triggered = False  # Prevent repeated alerts

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        landmarks = results.pose_landmarks.landmark
        left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP].y]
        left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE].x, landmarks[mp_pose.PoseLandmark.LEFT_KNEE].y]
        left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE].x, landmarks[mp_pose.PoseLandmark.LEFT_ANKLE].y]

        squat_angle = calculate_angle(left_hip, left_knee, left_ankle)

        # Determine squat position
        if squat_angle > 160:
            squat_position = "up"
            voice_alert_triggered = False  # Reset alert when standing
        elif squat_angle < 90:
            squat_position = "down"

        # Provide feedback
        color = (0, 255, 0)  # Green (correct)
        if squat_position == "down" and squat_angle > 100:
            color = (0, 0, 255)  # Red (incorrect)
            if not voice_alert_triggered:
                engine.say("Lower your squat!")
                engine.runAndWait()
                voice_alert_triggered = True  # Prevent continuous alerts

        cv2.putText(image, f"Angle: {int(squat_angle)}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

    cv2.imshow("AI Fitness Coach", image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()