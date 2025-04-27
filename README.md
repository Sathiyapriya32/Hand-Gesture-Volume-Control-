# Hand Gesture Volume Control with MediaPipe and OpenCV

This project uses **MediaPipe** and **OpenCV** to control the system's volume with hand gestures, specifically the distance between the thumb and index finger. The closer the fingers are, the higher the volume, and the farther they are, the lower the volume.

## Prerequisites

Make sure you have the following dependencies installed:

- Python 3.x
- `opencv-python`
- `mediapipe`

You can install the required libraries using the following command:

```bash
pip install opencv-python mediapipe
```
Dependencies for macOS:
This project uses osascript to control system volume. It's supported on macOS, but won't work on Windows or Linux without a different volume control method.

Code Overview
1. Imports:
The necessary libraries, OpenCV and MediaPipe, are imported to handle video capture, hand gesture detection, and volume control.

2. Hand Gesture Setup:
We use MediaPipe Hands to detect and track hand landmarks, specifically the thumb and index finger. The Hands object is initialized with parameters to process real-time video frames.

3. Main Loop:
The code captures frames from the webcam, processes them to detect hand landmarks, calculates the distance between the thumb and index finger, and maps this distance to the system volume.

Hand Landmark Detection: MediaPipe tracks hand landmarks to detect the positions of the thumb and index finger.

Distance Calculation: The distance between the thumb and index finger is calculated to control the volume.

Volume Mapping: The calculated distance is mapped to a volume range from 0 to 100, with the thumb and index finger being closer for a higher volume and farther for a lower volume.

System Volume Control: The system's volume is adjusted using osascript on macOS. You can modify the code for other operating systems if needed.

4. Exit:
To stop the program, press the 'q' key.

## 📸 Screenshots
![Screenshot 2025-04-27 at 1 57 40 PM](https://github.com/user-attachments/assets/671d9053-4b05-4e24-b95f-da5dad91b10d)

## 🎥 Project Explanation Video
 🎥 [Watch the Video](https://www.linkedin.com/posts/sathiyapriya-s-22ucs048_volumecontrol-ai-handgesture-activity-7237477339310219266-Ti6J?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEKubiABTjioeFLfoGOrHXFNNCGvYJ6moX8)
