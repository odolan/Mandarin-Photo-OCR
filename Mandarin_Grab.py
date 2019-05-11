from googletrans import Translator
import numpy as np
import pytesseract
import pyautogui
import imutils
import time
import sys
import cv2
import re
import os

try:
    from PIL import Image
except ImportError:
    import Image

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("/Users/owen/Desktop/OCR Mandarin/china_image.png", image)

directory = os.fsencode("/Users/owen/Desktop/OCR Mandarin/LOADIMAGEHERE")
global impath

quicksavename = "sample.png"
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".png"):
        
         imPath = "/Users/owen/Desktop/OCR Mandarin/LOADIMAGEHERE/"+filename
         impath = imPath
         pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.0.0_1/bin/tesseract'
         config = ('--tessdata-dir "tessdata" -l chi-sim --oem 1 --psm 3')
         text = pytesseract.image_to_string(imPath, config=config)

         string = ""
         for n in re.findall(r"[\u4e00-\u9fff]+",text):
             string = string + n
            
         print(string)
         translator = Translator()
         translated = translator.translate(src='zh-CN', dest='en', text=string)
         print("")
         print("")
         print(translated)
         continue
