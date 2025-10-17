import cv2

imaPath = input('\nenter the image path :')

#how to image load
image = cv2.imread(imaPath)

if image is not None:
    print('the image is successfully loaded')
else:
    print('the image is not loaded please loaded the image')

showImage = input('(1) show image yes or no :')
if showImage == 'yes':
    cv2.imshow('image show',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("you select the no")
diamension = input('(2) check the image daimension yes or no :')
if showImage == 'yes':
    h,w,c = image.shape
    print(f"image height {h} , width {w} and channel {c}")
else:
    print("you select the no :")
grayScal = input('(3) convert the image into gray scale yes or no :')
if showImage == 'yes':
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray image',gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("you select the no :")
saveImage = input('(4),save the image yes or no :')
