# AI-Powered Personalized Fitness Coach

> Real-time squat posture detection and voice feedback using computer vision — no wearables required.

---

## Overview

This project uses **Mediapipe** and **OpenCV** to detect body landmarks through a standard webcam, evaluate squat posture in real time, and deliver instant voice corrections via **pyttsx3**. It makes professional-grade fitness coaching accessible to anyone with a laptop or PC camera.

---

## Features

- **Real-time pose detection** — tracks hip, knee, and ankle landmarks using Mediapipe
- **Angle-based squat evaluation** — calculates knee joint angle to assess squat depth
- **Automatic rep counter** — counts completed squat repetitions per session
- **Voice feedback** — speaks corrections and encouragement hands-free
- **Color-coded overlay** — green for correct form, orange/red for corrections needed
- **No wearables needed** — works entirely through a standard webcam

---

## How It Works

1. Camera feed is captured and passed to Mediapipe's Pose model
2. Hip, knee, and ankle coordinates are extracted from pose landmarks
3. The angle at the knee joint is calculated using vector mathematics
4. Squat depth is classified based on angle thresholds:

| Angle | Classification | Feedback |
|---|---|---|
| > 160° | Standing | Go down! |
| 121°–160° | Descending | Keep going... |
| 91°–120° | Partial Squat | Go a bit lower! |
| ≤ 90° | Deep Squat ✅ | Good depth! |

5. Voice alerts are triggered at key positions to guide the user

---

## Project Structure

```
AI-Powered-Personalized-fitness-coach/
│
├── fitness_coach.py      # Main application
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/Lakshya1820057650/AI-Powered-Personalized-fitness-coach.git
cd AI-Powered-Personalized-fitness-coach
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python fitness_coach.py
```

### 4. Controls
- Allow camera access when prompted
- Stand in front of the camera so your full body is visible
- Perform squats — the system will track your form in real time
- Press **`q`** to quit and see your total rep count

---

## Requirements

- Python 3.9+
- Webcam / built-in camera
- Libraries: OpenCV, Mediapipe, NumPy, pyttsx3

---

## Tech Stack

- **OpenCV** — video capture and frame processing
- **Mediapipe** — real-time human pose estimation
- **NumPy** — angle calculations
- **pyttsx3** — offline text-to-speech voice feedback

---

## Future Improvements

- Support for more exercises (push-ups, lunges, bicep curls)
- Multi-person tracking
- Session history and progress logging
- Mobile application version

---

## License

MIT License — feel free to use and build upon this project.
