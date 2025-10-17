import cv2

#how to image load
image = cv2.imread('download.png')

if image is not None:
    #how to show the image
    cv2.imshow('My Image',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Error: image is not found')