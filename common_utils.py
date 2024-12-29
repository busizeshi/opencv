# 公共操作
import cv2 as cv

def cv_img_show(name,img):
    cv.imshow(name,img)
    cv.waitKey(0)
    cv.destroyAllWindows()