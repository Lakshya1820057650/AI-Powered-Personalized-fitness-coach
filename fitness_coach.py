"""
AI-Powered Personalized Fitness Coach
Uses Mediapipe and OpenCV to detect body landmarks, evaluate squat posture
in real time, and provide instant voice feedback via pyttsx3.
"""

import cv2
import mediapipe as mp
import numpy as np
import pyttsx3

# ── Initialize Mediapipe Pose ──────────────────────────────────────────────
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# ── Initialize Voice Engine ────────────────────────────────────────────────
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Words per minute


def calculate_angle(a, b, c):
    """
    Calculate the angle (degrees) at point b formed by points a-b-c.

    Args:
        a, b, c : [x, y] coordinate pairs (list or array)

    Returns:
        float : angle in degrees (0–360)
    """
    a, b, c = np.array(a), np.array(b), np.array(c)
    radians = (
        np.arctan2(c[1] - b[1], c[0] - b[0]) -
        np.arctan2(a[1] - b[1], a[0] - b[0])
    )
    angle = np.abs(radians * 180.0 / np.pi)
    return 360 - angle if angle > 180 else angle


def get_landmark_coords(landmarks, landmark_type):
    """Extract [x, y] from a pose landmark."""
    lm = landmarks[landmark_type]
    return [lm.x, lm.y]


def evaluate_squat(angle):
    """
    Evaluate squat depth and return status, color, and feedback text.

    Returns:
        tuple: (position, color_bgr, feedback_text)
    """
    if angle > 160:
        return "Standing", (0, 255, 0), "Standing — go down!"
    elif angle <= 90:
        return "Deep Squat", (0, 255, 0), "Good depth!"
    elif angle <= 120:
        return "Partial Squat", (0, 165, 255), "Go a bit lower!"
    else:
        return "Descending", (0, 200, 255), "Keep going down..."


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Cannot access camera. Please check your device.")
        return

    squat_position = None
    voice_alert_triggered = False
    rep_count = 0
    prev_position = None

    print("[INFO] AI Fitness Coach started. Press 'q' to quit.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("[WARNING] Frame capture failed.")
            break

        # Convert BGR → RGB for Mediapipe processing
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2)
            )

            landmarks = results.pose_landmarks.landmark

            # Extract hip, knee, ankle coordinates
            left_hip   = get_landmark_coords(landmarks, mp_pose.PoseLandmark.LEFT_HIP)
            left_knee  = get_landmark_coords(landmarks, mp_pose.PoseLandmark.LEFT_KNEE)
            left_ankle = get_landmark_coords(landmarks, mp_pose.PoseLandmark.LEFT_ANKLE)

            squat_angle = calculate_angle(left_hip, left_knee, left_ankle)
            position, color, feedback = evaluate_squat(squat_angle)

            # Rep counter logic: count one rep per full down → up cycle
            if position == "Deep Squat":
                squat_position = "down"
                if not voice_alert_triggered:
                    engine.say("Good squat depth!")
                    engine.runAndWait()
                    voice_alert_triggered = True
            elif position == "Standing":
                if squat_position == "down":
                    rep_count += 1
                squat_position = "up"
                voice_alert_triggered = False

            # ── Overlay UI ────────────────────────────────────────────────
            h, w, _ = image.shape

            # Angle display
            cv2.putText(image, f"Angle: {int(squat_angle)}",
                        (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, color, 2, cv2.LINE_AA)

            # Feedback text
            cv2.putText(image, feedback,
                        (30, 95), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, color, 2, cv2.LINE_AA)

            # Rep counter
            cv2.putText(image, f"Reps: {rep_count}",
                        (30, 140), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 255, 255), 2, cv2.LINE_AA)

            # Position indicator box
            box_color = (0, 200, 0) if position in ["Deep Squat", "Standing"] else (0, 100, 255)
            cv2.rectangle(image, (w - 200, 10), (w - 10, 60), box_color, -1)
            cv2.putText(image, position,
                        (w - 195, 45), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (255, 255, 255), 2, cv2.LINE_AA)

        else:
            cv2.putText(image, "No pose detected — adjust camera",
                        (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("AI Fitness Coach — Squat Tracker", image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    print(f"[INFO] Session ended. Total reps completed: {rep_count}")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
