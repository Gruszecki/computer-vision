import cv2

# Wyświetlanie zdjęcia
img = cv2.imread('assets/pool.jpg')
cv2.imshow('image', img)
cv2.waitKey(1000)
