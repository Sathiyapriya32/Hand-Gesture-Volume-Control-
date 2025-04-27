import subprocess
import cv2
import mediapipe as mp

# MediaPipe hands setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize video capture
cap = cv2.VideoCapture(0)

def set_volume(volume_level):
    # Ensure volume_level is between 0 and 100
    volume_level = max(0, min(volume_level, 100))
    subprocess.call(["osascript", "-e", f"set volume output volume {volume_level}"])

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip the frame horizontally

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmarks for thumb and index finger
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Calculate distance between thumb and index finger
            distance = ((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)**0.5

            # Define a range for distance and map it to volume
            # Assuming a typical hand gesture distance range
            min_distance = 0.05  # Minimum distance for max volume (scaled based on your hand)
            max_distance = 0.5   # Maximum distance for mute
            volume_range = 100    # Volume range 0-100

            # Scale the volume based on distance
            if distance < min_distance:
                volume_level = 100  # Maximum volume
            elif distance > max_distance:
                volume_level = 0    # Mute
            else:
                volume_level = int((1 - (distance - min_distance) / (max_distance - min_distance)) * volume_range)

            # Set system volume
            set_volume(volume_level)

    cv2.imshow("Hand Gesture Volume Control", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
