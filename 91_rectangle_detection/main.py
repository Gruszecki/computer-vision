import cv2
import imutils

img = cv2.imread(r'assets\phone.jpg')           # wwczytanie obrazu
cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    img = imutils.resize(img, None, 400)            # resize
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # konwersja do skali odcieni szarości

    blur = cv2.GaussianBlur(grey, (7, 7), 0)        # blur
    edges = cv2.Canny(blur, 0, 30)                # detekcja krawędzi

    contours = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)       # odnajdywanie konturów
    contours = imutils.grab_contours(contours)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]                     # sortowanie konturów

    rect = None
    for contour in contours:
        perimeter = cv2.arcLength(contour, closed=True)
        approx = cv2.approxPolyDP(contour, 0.015*perimeter, True)

        if len(approx) == 4:
            rect = approx
            break

    if rect is None:
        cv2.imshow('img', img)
    else:
        detected = cv2.drawContours(img, [rect], -1, (0, 255, 0), 3)           # rect jest w [] aby stworzyć linie, inaczej byłyby punkty
        cv2.imshow('img', detected)

    cv2.imshow('blur', blur)
    cv2.imshow('canny', edges)

    if cv2.waitKey(1) == 27:
        break
