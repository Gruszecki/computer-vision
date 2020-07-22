import cv2


def get_position(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f'x = {x}, y = {y}')
        cv2.circle(params, (x, y), 20, (0, 0, 255), 2)
        cv2.imshow('image', img)



img = cv2.imread(r'assets\pool.jpg')

cv2.namedWindow('image')
cv2.setMouseCallback('image', get_position, img)

cv2.imshow('image', img)
cv2.waitKey(0)
