import cv2

#how to image load
image = cv2.imread('D:\Documents\cv\download.png')

if image is None:
    print('image is not loaded please loaded the image')
else:
    (h,w)=image.shape[:2]
    
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center,90,1.0)
    rotated = cv2.warpAffine(image,M,(w,h))
    
    cv2.imshow('original image',image)
    cv2.imshow('rotated image',rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows