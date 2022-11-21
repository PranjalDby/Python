import pytesseract
import pandas
import numpy
import cv2
import matplotlib.pyplot as plot
from pytesseract import Output


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,1)

img = cv2.imread("photo.png")
img = remove_noise(img)
# img = get_grayscale(img)
d = pytesseract.image_to_data(img,output_type=Output.DICT)
n_boxes= len(d['text'])
print('len',n_boxes)
print(d)
for i in range(n_boxes):
    if int(d['conf'][i])>=0:
        (x,y,w,h) = (d['left'][i],d['top'][i],d['width'][i],d['height'][i])
        img = cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,255,0),thickness=2)

cv2.imshow('img',img)
cv2.waitKey(0)



