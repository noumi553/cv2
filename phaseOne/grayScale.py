import cv2

#how to image load
image = cv2.imread('D:\Documents\cv\download.png')

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray scal image",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('image is not loaded please loade the image')