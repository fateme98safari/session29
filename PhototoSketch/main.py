import cv2

image1=cv2.imread("PhototoSketch\input\Ronaldo.jpg")
image1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
inverted=255- image1
blurred=cv2.GaussianBlur(inverted,(21,21),0)
inverted_blurred=255-blurred
sketch=image1/ inverted_blurred
sketch=sketch*255

cv2.imwrite("PhototoSketch\output\Result.jpg",sketch)