from PIL import Image
import pytesseract as tess
os

tess.pytesseract.tesseract_cmd= r"C:\Program Files\Tesseract-OCR\tesseract.exe"
im = Image.open("1.jpg")

text = tess.image_to_string(im, lang = 'eng')

print(text)
