#!/usr/bin/python3

import logging
from PIL import Image
from PIL import EpsImagePlugin
import math
import cv2
import pytesseract as tess
import numpy as np


def checkImageQuality():
    logging.info("check image quelity ")



# def a(image):
#     import cv2

    
#     gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

#     # Remove horizontal
#     horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25,1))
#     detected_lines = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
#     cnts = cv2.findContours(detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#     for c in cnts:
#         cv2.drawContours(image, [c], -1, (255,255,255), 2)

#     # Repair image1
#     repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,6))
#     result = 255 - cv2.morphologyEx(255 - image, cv2.MORPH_CLOSE, repair_kernel, iterations=1)

#     cv2.imshow('thresh', thresh)
#     cv2.imshow('detected_lines', detected_lines)
#     cv2.imshow('image', image)
#     cv2.imshow('result', result)
#     cv2.waitKey()
#     return result





def preprocessingImage(input):
    image = cv2.imread(input)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    threshold_img = cv2.threshold(
        gray_image, 127, 255, cv2.THRESH_BINARY_INV)[1]

    logging.info("preProcessing image ")
    return threshold_img


def preprocessingPDF(input):
    logging.info("preProcessing pdf")