import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("myg.png", 0)

#Histogram hesaplama
hist = cv2.calcHist([img], [0], None,[256], [0,256])
#Histogram hesaplamak için calcHist kullanılır.

print(hist)

#Histogram Çizimi
plt.title("Gri Tonlama Histogramı")
plt.xlabel("Piksel Değeri")
plt.ylabel("Piksel Sayısı")
plt.show()