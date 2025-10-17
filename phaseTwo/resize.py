import cv2

#how to image load
image = cv2.imread('D:\Documents\cv\download.png')

if image is None:
    print('image is not loaded please load the image')
else:
    resize = cv2.resize(image,[200,200])
    cv2.imshow('original image',image)
    cv2.imshow('resize image',resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows