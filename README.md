# AI-Powered-Personalized-fitness-coach
AI powered personalized fitness coach
Simplified AI-Powered Personalized Fitness Coach

Project Overview

This project is an AI-powered fitness coach designed to detect basic workout postures (like squats or push-ups) and provide real-time feedback. It eliminates the need for wearable devices by using computer vision to track body movements and angles accurately.

Problem Solved

Helps users maintain correct posture during workouts.

Provides real-time feedback to prevent injuries and enhance performance.

Eliminates the need for expensive wearables by using camera-based tracking.

Key Features

Computer Vision-Based Tracking: Uses Mediapipe and OpenCV to detect exact postures and movement angles.

Camera-Based Tracking: Eliminates the need for wearables, making it accessible for everyone.

Real-Time Voice Feedback: Uses pyttsx3 to provide immediate verbal cues and corrections.

Supports Multiple Exercises: Can analyze and assist with various workout routines.

Color Indicator: Visual feedback for correctness and improvements.

Dependencies

List of required software, libraries, and frameworks:

Python Version: 3.9+

Required Libraries:

OpenCV

Mediapipe

pyttsx3

numpy

tkinter (if UI is included)

To install dependencies, run:

pip install -r requirements.txt

Setup Instructions

Installation Steps

Clone the repository:

git clone https://github.com/your-username/your-repository.git

Navigate to the project directory:

cd your-repository

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Configuration

Ensure your device has a working camera.

If using external API keys (optional), configure them as environment variables:

export API_KEY='your_api_key_here'

Running the Application

Start the application using:

python app.py

Or if using Flask/Django:

flask run
# or
python manage.py runserver

Usage

Open the application.

Allow camera access for posture detection.

Start a workout and follow the on-screen feedback.

Receive voice and color-based feedback for corrections.

Team Members

Member 1 - Lakshya Saxena ; Role - Coding

Member 2 - Prince Yadav ; Role -  PPT Creator

Member 3 - Soumya Gupta ;  Role - Content Creator

Member 4 - Somya Bharti ;  Role - Coding

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contribution Guidelines

If you wish to contribute:

Fork the repository

Create a new branch (feature-branch)

Commit changes and push

Open a pull request

Future Plans

Add support for more complex exercises.

Improve AI model accuracy.

Develop a mobile application version.

Integrate with fitness tracking apps.
