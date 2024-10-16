import cv2
from matplotlib import pyplot as plt

img = cv2.imread("myg.png")

#Görüntüyü BGR kanallarına ayır
b, g, r = cv2.split(img)

"""
cv2.imshow('normal', img)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
"""

# Histogramları hesapla
hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])  # Mavi kanalı
hist_g = cv2.calcHist([img], [1], None, [256], [0, 256])  # Yeşil kanalı
hist_r = cv2.calcHist([img], [2], None, [256], [0, 256])  # Kırmızı kanalı

#calcHist histogram hesaplamak için kullanılır

#Histogramları görselleştir
plt.plot(hist_b, color='blue', label='Mavi Kanal')
plt.plot(hist_g, color='green', label='Green channel')
plt.plot(hist_r, color='red', label='Red channel')

plt.xlim([0, 256])
plt.title('Renk Kanalları Histogramı')
plt.xlabel('Piksel Değeri')
plt.ylabel('Piksel Sayısı')
plt.legend()
plt.show()


cv2.imwrite("mavi_kanal.png", b)
cv2.imwrite("yesil_kanal.png", g)
cv2.imwrite("kirmizi_kanal.png", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
