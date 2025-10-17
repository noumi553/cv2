import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret,frame= cap.read()
    
    if not ret:
        print("can not read frame")
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    _,threshold = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        corners = len(approx)
        
        if corners == 3:
            shape_name = "Triangle"
        elif corners == 4:
            shape_name = "Rectangle"
        elif corners == 5:
            shape_name = "Pentagon"
        elif corners > 5:
            shape_name = "Circle"
        else:
            shape_name = "Unknown"
        
        cv2.drawContours(frame,[approx],0,(0,255,0),3)
        x=approx.ravel()[0]
        y=approx.ravel()[1] - 10
    
    cv2.putText(frame,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.6,255,0,0)
    
    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print('quating......')
        break

cap.release()
cv2.destroyAllWindows()