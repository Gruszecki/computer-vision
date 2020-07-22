import cv2
import numpy as np


def nothing(x):
    pass


img = np.zeros((300, 500, 3), 'uint8')

window_name = 'Palette'
cv2.namedWindow(window_name)
cv2.createTrackbar('Red', window_name, 0, 255, nothing)
cv2.createTrackbar('Green', window_name, 0, 255, nothing)
cv2.createTrackbar('Blue', window_name, 0, 255, nothing)

while True:
    r = cv2.getTrackbarPos('Red', window_name)
    g = cv2.getTrackbarPos('Green', window_name)
    b = cv2.getTrackbarPos('Blue', window_name)

    img[:] = [b, g, r]

    cv2.imshow(window_name, img)

    if cv2.waitKey(1) == 27:
        break
