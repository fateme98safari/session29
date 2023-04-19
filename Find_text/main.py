import cv2
import numpy as np

image1=cv2.imread("Find_text/input/A.png")
image2=cv2.imread("Find_text/input/B.png")

image1=image1.astype(np.float32)
image2=image2.astype(np.float32)
result=cv2.subtract(image1,image2)
result=result.astype(np.uint8)
result=255*result
result=255-result


cv2.imwrite("Find_text/output/result.jpg", result)