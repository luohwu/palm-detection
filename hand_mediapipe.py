import cv2
import math
import numpy as np
import os
DESIRED_HEIGHT = 456
DESIRED_WIDTH = 256
def resize_and_show(image):
  h, w = image.shape[:2]
  print(f'height: {h}, width: {w}')
  if h < w:
      img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
  else:
    img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
  cv2.imshow('img',img)

# Read images with OpenCV.



import mediapipe as mp
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
# help(mp_hands.Hands)

data_path = "/home/luohwu/Thesis_workspace/dataset/P01_11"

# for index in range(1, 31000, 60):
#   image_index = str(index).zfill(10)
#   image_path = os.path.join(data_path, f'frame_{image_index}.jpg')
#   if os.path.exists(image_path):
#     print(image_path)

# Run MediaPipe Hands.
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.7) as hands:
  data_path = "/home/luohwu/Thesis_workspace/dataset/P01_11"
  for image_index in range(1,31000,1):
    name=os.path.join(data_path, f'frame_{str(image_index).zfill(10)}.jpg')
    image=cv2.imread(name)

    # Convert the BGR image to RGB, flip the image around y-axis for correct
    # handedness output and process it with MediaPipe Hands.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print handedness (left v.s. right hand).
    print(f'Handedness of {name}:')
    print(results.multi_handedness)

    if not results.multi_hand_landmarks:
      continue

    # Draw hand landmarks of each hand.
    print(f'Hand landmarks of {name}:')
    image_height, image_width, _ = image.shape
    annotated_image = cv2.flip(image.copy(), 1)
    for rect in results.palm_detections:
        hand_bbodx_relative=rect.location_data.relative_bounding_box
        x0 = round(image_width * (hand_bbodx_relative.xmin))
        y0 = round(image_height * (hand_bbodx_relative.ymin))
        x1 = round(image_width * (hand_bbodx_relative.xmin+hand_bbodx_relative.width))
        y1 = round(image_height * (hand_bbodx_relative.ymin+hand_bbodx_relative.height))
        cv2.rectangle(image,(x0,y0),(x1,y1),(0, 0, 255), 3)
    cv2.imshow('img',image)
    cv2.waitKey(0)

