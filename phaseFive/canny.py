import cv2

image = cv2.imread('phaseFive/download(2).png')

#convert into gray scal

grayScalImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edge = cv2.Canny(grayScalImage,250,250)

cv2.imshow('Edge',edge)
cv2.imshow('GrayScaleImage',grayScalImage)
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()