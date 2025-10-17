import cv2

#how to image load
image = cv2.imread('D:\Documents\cv\download.png')

if image is None:
    print('image is not loaded please loaded the image')
else:
    pt1=(50,50)
    pt2=(150,100)
    color=(200,0,0)
    thikness=4
    cv2.rectangle(image,pt1,pt2,color,thikness)
    
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()