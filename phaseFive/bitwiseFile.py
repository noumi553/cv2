import cv2
import numpy as np

#draw a window size
imgOne = np.zeros((300,300),dtype="uint8")
imgtwo = np.zeros((300,300),dtype="uint8")

#create a circle
circle = cv2.circle(imgOne,(150,150),100,255,-1)

#create a rectangle
rectangle = cv2.rectangle(imgtwo,(50,50),(150,150),(255,240,0),-1)

bitwise_and = cv2.bitwise_and(imgOne,imgtwo)
bitwise_not = cv2.bitwise_not(imgOne)
bitwise_or = cv2.bitwise_or(imgOne,imgtwo)

print(imgtwo.shape)
cv2.imshow('imgOne',imgOne)
cv2.imshow('imgTwo',imgtwo)
cv2.imshow("bitwise_and",bitwise_and)
cv2.imshow('bitwise_not',bitwise_not)
cv2.imshow('bitwise_or',bitwise_or)
cv2.waitKey(0)
cv2.destroyAllWindows()