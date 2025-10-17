import cv2

img = cv2.imread('phaseFive/download(1.png',cv2.IMREAD_GRAYSCALE)
thresh_value = 50
max_value = 256
thresh_type = cv2.THRESH_BINARY
if img is None:
    print('no image found please check the file path')
else:
    _,thresh = cv2.threshold(img,thresh_value,max_value,thresh_type)
    if thresh is None:
        print('image is not thresh')
    print('image is loaded')
    cv2.imshow('originalImage',img)
    cv2.imshow('threshImage',thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()