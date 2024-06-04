# Yoga_pose_detection

This project aims to help you perfect your yoga poses using a webcam and some clever programming. It uses OpenCV for video capture, MediaPipe for detecting body poses, and NumPy for calculating angles.

What Does the Code Do?
Setting Things Up:
We start by importing OpenCV (for handling video), MediaPipe (for pose detection), and NumPy (for math operations).
We initialize MediaPipe's pose detection and drawing tools so we can identify and visualize body joints.
Defining Perfect Poses:

We define the “ideal” angles for two yoga poses: the T-pose and Warrior II. These angles are what the program will compare your poses to.
Calculating Angles:

The code includes a function to calculate angles between three points (think of these as your joints). For example, your shoulder, elbow, and wrist form an angle at the elbow.
Getting Joint Positions:

Using MediaPipe, the code identifies key points on your body (like shoulders, elbows, and wrists). These key points are used to calculate the angles at your joints.
Comparing Your Pose:
The program compares the angles of your pose to the ideal angles for the defined poses. If your angles are close enough to the ideal ones, the pose is considered correct.
Giving Feedback:
The program gives you visual feedback. It displays text on the screen to let you know if your pose is correct or not and highlights the joints with different colors.
Real-Time Pose Detection:
The program captures video from your webcam.
It processes each video frame to detect your pose and calculate the necessary angles.
It displays the video with feedback overlaid until you decide to stop by pressing the 'q' key.
How It All Works Together
Initialization:
The code sets up the tools it needs to detect your pose and compare it to the ideal poses.
Detecting Poses:
Your webcam captures a video feed, which the program processes frame by frame.
It uses MediaPipe to find your joints and calculates the angles between them.
Checking Accuracy:
It compares the angles of your current pose to the ideal angles for the T-pose and Warrior II.
If your pose matches closely enough, it tells you that your pose is correct.
Displaying Feedback:
The program draws lines and points on your video feed to show your joints and angles.
It also displays a message indicating if your pose is correct.
Continuous Monitoring:
The process repeats continuously, updating the video feed in real-time.
The loop continues until you press the 'q' key to quit.


Other than this i have made comments in the .py file which has been uploaded which will describe wht i am doing in that section of code.
