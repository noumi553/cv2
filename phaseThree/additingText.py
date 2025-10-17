import cv2

#how to image load
image = cv2.imread('D:\Documents\cv\download.png')

if image is None:
    print('image is not loaded please loaded the image')
else:
    cv2.putText(image,'Nouman aziz',(50,100),
                cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,25,25),2)
    
    cv2.imshow('image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()