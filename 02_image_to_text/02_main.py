import pytesseract
import cv2


def convert(filename):
    image = cv2.imread(filename)
    print(pytesseract.image_to_string(image))


convert(r'assets/test.jpg')