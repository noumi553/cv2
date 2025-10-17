import cv2

#how to image load
image = cv2.imread('D:\Documents\cv\download.png')

if image is None:
    print('image is not loaded please loaded the image')
else:
    print('image loaded successfully')
    cv2.circle(image,(150,50),50,(255,40,250),-1)
    
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()