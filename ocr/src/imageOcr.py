import cv2
import numpy as np
import pytesseract

img = cv2.imread("sample1.jpg")

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# im = Image.open("sample1.jpg")

text = pytesseract.image_to_string(img, lang = 'eng')

print(text)
