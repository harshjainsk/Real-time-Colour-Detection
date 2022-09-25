import cv2
import numpy as np


frameWidth = 640
frameHeight = 400

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
# cap.destroyAllWindows()
