# Yoga_pose_detection

This project aims to help you perfect your yoga poses using a webcam and some clever programming. It uses OpenCV for video capture, MediaPipe for detecting body poses, and NumPy for calculating angles.

What Does the Code Do?
Setting Things Up:
We start by importing OpenCV (for handling video), MediaPipe (for pose detection), and NumPy (for math operations).
We initialize MediaPipe's pose detection and drawing tools so we can identify and visualize body joints.
Continuous Monitoring:
The process repeats continuously, updating the video feed in real-time.
The loop continues until you press the 'q' key to quit.


Setup
Install Required Libraries: Make sure you have Python installed. Then, install OpenCV, MediaPipe, and NumPy using your preferred method.

Download the Code: Get the project files by downloading or cloning the repository to your computer.

Run the Script: Navigate to the directory where you saved the project files and run the script to start the application.

Usage
Start the Application: Launch the script, and it will begin capturing video from your webcam.

Perform Your Yoga Poses: Stand in front of the camera and perform the T-pose or Warrior II. The app will analyze your pose in real-time.

Get Feedback: The application will show your video feed with visual feedback:

Green points and lines indicate that your pose is correct.
Red points and lines mean your pose needs adjustment.
Text feedback will also appear on the screen to guide you.
Stop the Application: To exit the application, press the 'q' key on your keyboard.

Challenges
Lighting: Ensure your room is well-lit so the webcam can accurately detect your joints. Poor lighting can lead to incorrect pose detection.

Camera Positioning: Position the camera to capture your full body. If it’s too close or too far, some joints might be out of frame, affecting accuracy.

Background Clutter: A clean background helps the system focus on your pose. Too many objects in the background can confuse the detection algorithm.

Pose Variations: The system compares your pose to predefined standards. Small variations might not be recognized as correct even if they are acceptable in practice.

Computer Performance: Real-time video processing can be demanding, so make sure your computer is powerful enough to handle it smoothly.

Other than this i have made comments in the .py file which has been uploaded which will describe wht i am doing in that section of code.
