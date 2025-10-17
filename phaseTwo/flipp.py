import cv2

#how to image load
image = cv2.imread('download.png')

if image is None:
    print('image is not loaded please loaded the image')
else:
    flipHorizantal = cv2.flip(image,1)
    flipVertical = cv2.flip(image,0)
    flipBoth = cv2.flip(image,-1)
    
    cv2.imshow('original image',image)
    cv2.imshow('flipHorizantal',flipHorizantal)
    cv2.imshow('flipVertical',flipVertical)
    cv2.imshow('flipBoth',flipBoth)
    cv2.waitKey(0)
    cv2.destroyAllWindows