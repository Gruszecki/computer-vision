import cv2

img = cv2.imread(r'assets\feel.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]

contours = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]
img_and_contours = cv2.drawContours(img.copy(), contours, -1, (200, 0, 255), 2)
cv2.imshow('img and contours', img_and_contours)

max_area = [0.0, -1]        # Max area i index
for i in range(len(contours)):
    area = cv2.contourArea(contours[i], True)

    if area > max_area[0]:
        max_area[0] = area
        max_area[1] = i

print(max_area)
print(cv2.arcLength(contours[max_area[1]], closed=True))   # Długość konturu

img_max_area = cv2.drawContours(img.copy(), contours, max_area[1], (200, 0, 255), 2)
cv2.imshow('max area', img_max_area)

cv2.waitKey(0)
