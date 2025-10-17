import cv2

#how to image load
image = cv2.imread('D:\Documents\cv\download.png')

if image is not None:
    h,w,c = image.shape
    print(f'image height {h} , width {w} and channel {c}')
else:
    print('image is not loaded please loade the image')