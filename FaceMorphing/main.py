import cv2
import numpy as np

image1=cv2.imread("input\sajjad.jpg")
image2=cv2.imread("input\lion.jpg")

image1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
image2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

image1=image1.astype(np.float32)
image2=image2.astype(np.float32)

# image1=cv2.cvtColor()
# result=image1+image2
# cv2.imwrite("output/result.jpg", result)

result1=(image1 *5/6) + (image2*1/6)
result2=(image1 *4/6) + (image2*2/6)
result3=(image1 *3/6) + (image2*3/6)
result4=(image1 *2/6) + (image2*4/6)
result5=(image1 *1/6) + (image2*5/6)

result1=result1.astype(np.uint8)
cv2.imwrite("output/result1.jpg", result1)

result2=result2.astype(np.uint8)
cv2.imwrite("output/result2.jpg", result2)

result3=result3.astype(np.uint8)
cv2.imwrite("output/result3.jpg", result3)

result4=result4.astype(np.uint8)
cv2.imwrite("output/result4.jpg", result4)

result5=result5.astype(np.uint8)
cv2.imwrite("output/result5.jpg", result5)

# cv2.waitKey()