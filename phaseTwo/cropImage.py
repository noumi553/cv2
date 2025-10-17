import cv2

#how to image load
image = cv2.imread('D:\Documents\cv\download.png')

if image is not None:
    croped = image[100:200,50:150]
    
    cv2.imshow('original image',image)
    cv2.imshow('cropped image',croped)
    cv2.waitKey(0)
    cv2.destroyAllWindows
else:
    print('image is does not loaded please load the image')