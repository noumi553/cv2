import cv2
import numpy as np

sharped_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

image = cv2.imread('phaseFour/download.png')

if image is None:
    print('image is not loaded please loade the image')
else:
    print('image loaded')
    print('if you remove pic please click any key on keybord')
    filter=cv2.filter2D(image,-1,sharped_kernel)
    cv2.imshow('originalImage',image)
    cv2.imshow('filterImage',filter)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('quiting.......')