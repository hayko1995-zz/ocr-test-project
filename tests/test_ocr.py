import sys
sys.path.append('ocr')
import os
import cv2 as cv
from ocr.src import processing 
from click.testing import CliRunner
from ocr.ocr import main
from ocr import __version__



def test_version():
    assert __version__ == '0.1.0'



def test_main():  # test software worsk or not
    runner = CliRunner()
    result = runner.invoke(main, input="../ocr/samples/1.png")
    assert result.exit_code == 0


def test_checkImageQuality():  # test software worsk or not
    path = os.path.abspath("ocr/samples/1.png")
    img = cv.imread(path)
    result = processing.checkImageQuality(img)
    assert result == True


def test_preprocessingImage():  # test software worsk or not
    path = os.path.abspath("tests/samples/test.png")
    testImage = cv.imread(path)
    print(path)
    originalImage = processing.preprocessingImage("ocr/samples/1.png")
    cv.imwrite("test.png", originalImage)
    originalImage = cv.imread("test.png")
    os.remove("test.png")
    
    result = False
    if originalImage.shape == testImage.shape:
        difference = cv.subtract(testImage, originalImage)
        b, g, r = cv.split(difference)
        if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
            result = True
        else:
            result = False
    assert result == True


