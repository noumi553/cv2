import cv2
import numpy as np

# Load cascades
face_cascade = cv2.CascadeClassifier("phaseSeven/haarcascade_frontalface_default.xml")
eyes_cascade = cv2.CascadeClassifier("phaseSeven/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("phaseSeven/haarcascade_smile.xml")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print('Cannot read the frame')
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        # --- Face border ---
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 50, 255), 1)
        cv2.putText(frame, "Face", (x, y-10), cv2.QT_FONT_NORMAL, 0.6, (0, 255, 0), )

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        eyes = eyes_cascade.detectMultiScale(roi_gray,1.1,10)
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 1)
            text_x = ex
            text_y = ey + eh + 15
            cv2.putText(roi_color, "Eye", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)

    cv2.imshow('Face, Eyes & Smile Detection (Stylish)', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
