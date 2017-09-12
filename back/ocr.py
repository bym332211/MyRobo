from PIL import Image as myImage
import pytesseract
import cv2
import random
import numpy as np


def ocr_text(image_path):
    text = ''
    # try :
    img = myImage.open(image_path)
    img.load()
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
    text = pytesseract.image_to_string(img,lang="inso")
    # except Exception as e:
    #     print(e)
    print(text)

ocr_text('c1.jpg')