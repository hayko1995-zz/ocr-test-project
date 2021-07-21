#!/usr/bin/python3
import logging
import cv2
import numpy as np
import platform
import pytesseract as tess


if (platform.system() == "Windows"):
    tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def ocrPDF(input, output):
    logging.info("postprocessing")

    # PDF_file = input
    # pages = convert_from_path(PDF_file, 500)


def ocrImage(path, output): # TODO: Understand the document type and create a template for the file type
    f = open(output, 'w')
    print(path)
    image = cv2.imread(path)
    text = tess.image_to_string(image, lang='eng')
    f.write(text)
    f.close()
