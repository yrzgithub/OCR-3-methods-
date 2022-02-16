# METHOD 1
import cv2
from pytesseract import pytesseract

cam = cv2.VideoCapture(0)
while True:
    pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract"
    ret, img = cam.read()
    if ret == False:
        print("continue")
        continue
    cv2.imshow("ok", img)
    cv2.waitKey(1)
    print(pytesseract.image_to_string(img))
    # cam.release()
    # cv2.destroyAllWindows()

### METHOD 2

import easyocr, cv2, pyttsx3
import keyboard

convertor = pyttsx3.init()

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    ret, img = cam.read()
    cv2.imshow("ok", img)
    cv2.waitKey(1)
    if keyboard.is_pressed("esc"):
        break
cam.release()
read = easyocr.Reader(lang_list=["en"])
a = read.readtext(img)
for i in a:
    print(i[1])
    convertor.say(i[1])
    convertor.runAndWait()

# METHOD 3
# In this code you should save an image with text.
import easyocr, pyttsx3, PIL.Image

convertor = pyttsx3.init()
read = easyocr.Reader(lang_list=["en"])
img = PIL.Image.open(r"C:\Users\seenusanjay\Downloads\Screenshot 2021-09-18 142327.jpg")
img.show()
text = read.readtext(img)
for i in text:
    print(i[1])
    convertor.say(i[1])
    convertor.runAndWait()
