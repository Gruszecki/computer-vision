import cv2

img_back = cv2.imread(r'assets\sunset.jpg')
img_front = cv2.imread(r'assets\feel.png')

cv2.imshow('back', img_back)
cv2.imshow('front', img_front)

img_front_h, img_front_w = img_front.shape[:2]
roi = img_back[:img_front_h, :img_front_w]

img_front_gray = cv2.cvtColor(img_front, cv2.COLOR_BGR2GRAY)
mask = cv2.threshold(img_front_gray, 220, 255, cv2.THRESH_BINARY)[1]
mask_inv = cv2.bitwise_not(mask)

img_back_subs = cv2.bitwise_and(roi, roi, mask=mask)
img_front_subs = cv2.bitwise_and(img_front, img_front, mask=mask_inv)

img_subs = cv2.add(img_back_subs, img_front_subs)

img_back[:img_front_h, :img_front_w] = img_subs

cv2.imshow('final', img_back)

cv2.waitKey(0)
