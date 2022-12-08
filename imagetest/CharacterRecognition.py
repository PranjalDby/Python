from email.mime import image
from tkinter import Image
import pytesseract

import cv2
import matplotlib.pyplot as plot
from pytesseract import Output


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,1)

img = cv2.imread("photo.png")
imge = img.copy()
img = remove_noise(img)
# # img = get_grayscale(img)
target = str(input('Enter the word tha you want to find: '))
d = pytesseract.image_to_data(img,output_type=Output.DICT)
occurance = [ i for i,word in enumerate(d["text"]) if word.lower() == target]
print(occurance)
n_boxes= len(d['text'])
# print('len',n_boxes)
print(d)
for i in occurance:
    if int(d['conf'][i])>=0:
        (x,y,w,h) = (d['left'][i],d['top'][i],d['width'][i],d['height'][i])
        imge = cv2.rectangle(imge,(x,y),(x+w,y+h),color=(255,0,0),thickness=2)

cv2.imshow('img',imge)
cv2.waitKey(0)



