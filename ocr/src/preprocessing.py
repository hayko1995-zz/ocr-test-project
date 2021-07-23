#!/usr/bin/python3

import logging
import cv2
import pytesseract as tess
import numpy as np
from pdf2image import convert_from_path


def checkImageQuality(image):
    # A4 paper actual size is 210 x 297 mm

    logging.info("check image quelity ")
    x, _, _ = image.shape
    dpi = x * 25.4 / 210
    logging.debug("dpi = " + str(dpi))
    if (dpi < 200):
        return True
    return False


def preprocessingImage(input):
    logging.info("preProcessing image ")
    image = cv2.imread(input)  # read image

    if (checkImageQuality(image)):

        # scale image to a larger size to recognize small characters
        image = cv2.resize(image, None, fx=9, fy=9,
                           interpolation=cv2.INTER_CUBIC)

        # median blurring preserves edges as the median value must be the value of one of neighboring pixels.
        image = cv2.medianBlur(image, 3)

        image = cv2.bilateralFilter(image, 9, 75, 75)

        # convert image to grasscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # algorithm calculate the threshold for small regions of the image
        image = cv2.adaptiveThreshold(
            gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31, 2)

    return image


def preprocessingPDF(input):

    logging.info("preProcessing pdf")

    logging.debug(input)
    pages = convert_from_path(input, 500)

    # Counter to store images of each page of PDF to image
    image_counter = 1

    # Iterate through all the pages stored above
    for page in pages:
        filename = "page_"+str(image_counter)+".jpg"

    # Save the image of the page in system
        page.save(filename, 'JPEG')
        logging.debug(filename)
        preprocessingImage(filename)

    # Increment the counter to update filename
        image_counter = image_counter + 1

    logging.info("preProcessing done")

    return image_counter
    # return 0
