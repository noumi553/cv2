import cv2

image = cv2.imread('phaseFour/download.png')

if image is None:
    print('image is not loaded please loade the image')
else:
    print('image loaded')
    print('if you remove pic please click any key on keybord')
    blurImage = cv2.GaussianBlur(image, (7,7),0)
    medianBlur = cv2.medianBlur(image,11)
    cv2.imshow('original image',image)
    cv2.imshow('blur image',blurImage)
    cv2.imshow('medianBlur image',medianBlur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('quiting.......')