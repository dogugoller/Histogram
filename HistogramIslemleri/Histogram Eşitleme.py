import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("myg.png",0)


#Histogram eşitleme

equalized_img = cv2.equalizeHist(img)
#Görüntü konstrası atlamak için equalizeHist kullaılır.
#Görüntü konstrası artar ve görüntü daha görünebilir hale gelir.


cv2.imshow("Default",img)
cv2.imshow("Histogram Esitlenmis Image", equalized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()