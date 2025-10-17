import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Cannot open camera")
    exit()

frame_width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')
recorder = cv2.VideoWriter("my_video.mp4", codec, 20.0, (frame_width, frame_height))

if not recorder.isOpened():
    print("Error: VideoWriter failed to open!")
    exit()

print("Recording... Press 'q' to stop.")

while True:
    success, frame = camera.read()
    if not success:
        print("Failed to read frame")
        break

    recorder.write(frame)
    cv2.imshow("live", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
recorder.release()
cv2.destroyAllWindows()
print("Recording saved as my_video.avi")
