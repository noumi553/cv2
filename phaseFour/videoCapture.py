import cv2

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FOCUS))

while(True):
    ret, frame = cap.read()
    
    if not ret:
        print('Could not reading frame')
        break
    
    cv2.imshow('web cam',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('Quating....')
        break
cap.release()
cv2.destroyAllWindows()