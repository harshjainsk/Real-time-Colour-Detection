import cv2
import numpy as np

frameWidth = 640
frameHeight = 400

cap = cv2.VideoCapture(0)


def empty(a):
    pass


cv2.namedWindow('HSV')
cv2.resizeWindow("HSV",400,240)
cv2.createTrackbar('Hue Min', "HSV", 0, 179, empty)

while True:

    ret, frame = cap.read()
    imgHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('HSV Color Space', imgHSV)
    cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
# cap.destroyAllWindows()
