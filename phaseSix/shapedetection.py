import cv2

img = cv2.imread('phaseSix/download (4).png')
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,threshold = cv2.threshold(grayImg,200,255,cv2.THRESH_BINARY)

contours,heirarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,255,0),3)

for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01 * cv2.arcLength(contour,True),True)
    corners = len(approx)
    
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "pentagon"
    elif corners > 5:
        shape_name = "circle"
    else:
        shape_name = "unkown"
    cv2.drawContours(img,[approx],0,(0,255,0),3)
    x=approx.ravel()[0]
    y=approx.ravel()[1] - 10
    print(shape_name)
    
    cv2.putText(img,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,255,0,0)


cv2.imshow('Shape detection in image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()