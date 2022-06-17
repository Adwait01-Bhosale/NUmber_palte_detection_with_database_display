# importing opencv and pytesseract
import cv2
import pytesseract
from tkinter.filedialog import *


def extract_text(path):
    # path=askopenfilename()
    # print(path)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    img = cv2.imread(path)

    text = pytesseract.image_to_string(img, config="--psm 3")
    return text

# path=askopenfilename()
# print(path)

# img = cv2.imread(path)

# text = pytesseract.image_to_string(img, config="--psm 3")
# print(text)
