import cv2
import mediapipe as mp
from mediapipe import solutions
import mediapipe
import csv
import keyboard
import numpy as np
import time
import os
from Utils import extractLandMarks

#SETUP THINGS
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#Global Variables
frame_rate = 30
prev = 0
frames = 30
samples = 30
Data_Path = "Data"

def recordLandMarks(gesture, frame, hand_landmarks):
    #Check if the folder for the gesture exist
    if(not os.path.exists(os.path.join(Data_Path, gesture))):
        os.makedirs(os.path.join(Data_Path, gesture))
    
    
    #Check Current Folder
    all_folders = os.listdir(os.path.join(Data_Path, gesture))
    all_folders = [int(numeric_string) for numeric_string in all_folders]
    if(not all_folders):
        latest = str(0)
    else:
        all_folders.sort()
        latest = int(all_folders[-1])
        #Check the latest frame in the current folder. If it is more than 30, create a new folder
        latest_frame = os.listdir(os.path.join(Data_Path, gesture, str(latest)))
        if('30.npy' in latest_frame): #we are in the 30th frame already. Make a new one
            latest += 1

    latest = str(latest)
    if(not os.path.exists(os.path.join(Data_Path, gesture, latest))):
        os.makedirs(os.path.join(Data_Path, gesture, latest))

    np.save(os.path.join(Data_Path, gesture, latest, str(frame)), extractLandMarks(hand_landmarks))
    

#mediaPipe CopyPaste
cap = cv2.VideoCapture(0)
frame = 0
recording = False
gesture = None
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    time_elapsed = time.time() - prev
    res, image = cap.read()

    if time_elapsed > 1./frame_rate:
        prev = time.time()
    else:
        continue
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break

    #Record Landmarks
    if(results.multi_hand_landmarks):
        for hand_landmarks in results.multi_hand_landmarks:
            if(keyboard.is_pressed("A") and not recording):
                recording = True
                print("recording Started")
                gesture = "A"

            if(keyboard.is_pressed("J") and not recording):
                recording = True
                print("recording Started")
                gesture = "J"

            if(keyboard.is_pressed("B") and not recording):
                recording = True
                print("recording Started")
                gesture = "B"

            if(keyboard.is_pressed("D") and not recording):
                recording = True
                print("recording Started")
                gesture = "D"

            if(keyboard.is_pressed("Z") and not recording):
                recording = True
                print("recording Started")
                gesture = "Z"

            if(keyboard.is_pressed("Y") and not recording):
                recording = True
                print("recording Started")
                gesture = "YES"

            if(keyboard.is_pressed("2") and not recording):
                recording = True
                print("recording Started")
                gesture = "2Joints"

            if(recording):
                if(frame >= frames):
                    recording = False
                    frame = 0
                    print("recording Finished")
                    continue
                frame += 1
                print(frame)
                recordLandMarks(gesture, frame, hand_landmarks)


cap.release()