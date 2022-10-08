import cv2
import numpy as np
import pytesseract
from googletrans import Translator

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread("manga.jpg")
texts = pytesseract.image_to_string(img)
print(texts)

# translator = Translator()
# translated_dailogue = translator.translate(texts)
# print(translated_dailogue)


