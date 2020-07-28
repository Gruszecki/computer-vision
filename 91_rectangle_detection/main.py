import cv2
import imutils

img = cv2.imread(r'assets\phone.jpg')           # wwczytanie obrazu
cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    img = imutils.resize(img, None, 400)            # resize
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # konwersja do skali odcieni szarości

    blur = cv2.GaussianBlur(grey, (7, 7), 0)        # blur
    edges = cv2.Canny(blur, 0, 120)                  # detekcja krawędzi

    contours = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)       # odnajdywanie konturów
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]                     # sortowanie konturów

    rect = None
    for contour in contours:
        perimeter = cv2.arcLength(contour, closed=True)
        approx = cv2.approxPolyDP(contour, perimeter*0.015, True)

        if len(approx) == 4:
            rect = approx
            break

    if rect is None:
        cv2.imshow('img', img)
    else:
        detected = cv2.drawContours(img.copy(), [rect], -1, (0, 255, 0), 3)           # rect jest w [] aby stworzyć linie, inaczej byłyby punkty

        points = rect.reshape(4, 2)
        left_top_x = min([points[0][0], points[1][0], points[2][0], points[3][0]])
        left_top_y = min([points[0][1], points[1][1], points[2][1], points[3][1]])
        right_bottom_x = max([points[0][0], points[1][0], points[2][0], points[3][0]])
        right_bottom_y = max([points[0][1], points[1][1], points[2][1], points[3][1]])

        cv2.imshow('img', detected)
        cv2.imshow('trunc', img[left_top_y:right_bottom_y, left_top_x:right_bottom_x])

    cv2.imshow('blur', blur)
    cv2.imshow('canny', edges)

    if cv2.waitKey(1) == 27:
        break
