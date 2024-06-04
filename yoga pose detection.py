#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python mediapipe numpy


# In[ ]:





# In[6]:


import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Initialize MediaPipe Drawing
mp_drawing = mp.solutions.drawing_utils

# Define correct poses with angles for comparison
correct_poses = {
    'T-pose': {
        'left_elbow_angle': 180,
        'right_elbow_angle': 180,
        'left_shoulder_angle': 90,
        'right_shoulder_angle': 90,
    },
    'Warrior II': {
        'left_elbow_angle': 180,
        'right_elbow_angle': 180,
        'left_shoulder_angle': 90,
        'right_shoulder_angle': 90,
    }
}

def calculate_angle(a, b, c):
    """Calculate the angle between three points a, b, and c."""
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    if angle > 180.0:
        angle = 360 - angle
    return angle

def get_landmarks(results):
    landmarks = {}
    for id, lm in enumerate(results.pose_landmarks.landmark):
        landmarks[id] = (lm.x, lm.y)
    return landmarks

def get_angles(landmarks):
    angles = {}
    # Define angles for elbows and shoulders
    angles['left_elbow_angle'] = calculate_angle(
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
        landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    )
    angles['right_elbow_angle'] = calculate_angle(
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    )
    angles['left_shoulder_angle'] = calculate_angle(
        landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value],
        landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value],
        landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    )
    angles['right_shoulder_angle'] = calculate_angle(
        landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
        landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value]
    )
    return angles

def is_pose_correct(detected_angles, correct_angles, threshold=15):
    for key in correct_angles:
        if key not in detected_angles:
            return False
        if abs(detected_angles[key] - correct_angles[key]) > threshold:
            return False
    return True

def provide_feedback(image, detected_pose):
    """Provide visual feedback based on the detected pose."""
    if detected_pose in correct_poses:
        feedback = f"{detected_pose} - Correct Pose"
        color = (0, 255, 0)
    else:
        feedback = "Incorrect Pose"
        color = (0, 0, 255)

    cv2.putText(image, feedback, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

# Initialize webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and find poses
    results = pose.process(image)

    # Convert the image back to BGR for OpenCV
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Draw pose landmarks and provide feedback
    if results.pose_landmarks:
        landmarks = get_landmarks(results)
        detected_angles = get_angles(landmarks)
        detected_pose = None
        pose_correct = False

        for pose_name, correct_angles in correct_poses.items():
            if is_pose_correct(detected_angles, correct_angles):
                detected_pose = pose_name
                pose_correct = True
                break

        provide_feedback(image, detected_pose)
        color = (0, 255, 0) if pose_correct else (0, 0, 255)
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=color, thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=color, thickness=2, circle_radius=2)
        )

    # Display the image
    cv2.imshow('Yoga Pose Detection', image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:






# In[ ]:





# In[ ]:




