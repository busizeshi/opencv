# 图像基本操作
import cv2 as cv

import common_utils as utils

# 图像基本读取
img=cv.imread("D:/resource/image/girl1.jpg")
# print(img)
# cv.imshow("徐大力",img)
# cv.waitKey(2000) # 延迟时间，毫秒
# cv.destroyAllWindows()
# utils.cv_img_show("girl",img)
print(img.shape) #(1440, 1080, 3)