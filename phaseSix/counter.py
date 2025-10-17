import cv2

image = cv2.imread('phaseSix/download (4).png')
grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

_ ,thresh =cv2.threshold(grayImage,240,255,cv2.THRESH_BINARY)

counter , heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(image,counter,-1,(0,255,0),3)

for counters in counter:
    approx = cv2.approxPolyDP(counters,0.01 * cv2.arcLength(counters,True),True)
    
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
    cv2.drawContours(image,[approx],0,(0,255,0),2)
    x=approx.ravel()[0]
    y=approx.ravel()[1] - 10
    print(shape_name)
    cv2.putText(image,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,255,0,0)

cv2.imshow("contour",image)
cv2.waitKey(0)
cv2.destroyAllWindows()