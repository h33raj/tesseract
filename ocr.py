# pip install opencv-python
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

img = cv2.imread("images/test.png")

text =  pytesseract.image_to_string(img)
print(text)

cv2.imshow("img", img)
cv2.waitKey(0)
