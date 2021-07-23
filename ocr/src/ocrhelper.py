#!/usr/bin/python3
import logging
import cv2
import os
import platform
import pytesseract as tess


if (platform.system() == "Windows"):
    tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def ocrPDF(input, count, output):
    logging.info("ocr PDF starts")
    f = open(output, "a")

# Iterate from 1 to total number of pages
    for i in range(1, count ):
        filename = "page_"+str(i)+".jpg"
        logging.debug(filename)
    # Recognize the text as string in image using pytesserct
        text = str(((tess.image_to_string(cv2.imread(filename)))))
        text = text.replace('-\n', '')

        os.remove(filename)

    # Finally, write the processed text to the file.
        f.write(text)

    # Close the file after writing all the text.
    f.close()
    logging.info("postprocessing")

    # PDF_file = input
    # pages = convert_from_path(PDF_file, 500)


# TODO: Understand the document type and create a template for the file type
def ocrImage(image, output):
    f = open(output, 'w')
    text = tess.image_to_string(image, lang='eng')
    f.write(text)
    f.close()
