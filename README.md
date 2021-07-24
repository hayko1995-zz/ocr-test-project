# ocr-test-project
#install on linux
$sudo apt install opencv-python3
$sudo apt-get install tesseract-ocr

#install on windows
guide for install tenseract on windows https://rb.gy/5kqz3q
$pip install pytesseract

##########################For reviewer####################################
for run in python 
$cd ocr  
$python --input=<path to file> --output=<path to file> 

##################Run on Poetry###############################
$Poetry run pytest


# I have one mistake when im try to run with poetry 
# poetry run ocr --image="path" didnt works :) 
