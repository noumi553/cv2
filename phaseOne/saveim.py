import cv2

#how to image load
image = cv2.imread('D:\Documents\cv\download.png')

if image is not None:
    saveim = cv2.imwrite('output.png',image)
    if saveim:
        print('the image successfully save')
else:
    print('the image is not successfully save')

output = cv2.imread("output.png")

if output is not None:
    cv2.imshow("output image",output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('image is not loaded')