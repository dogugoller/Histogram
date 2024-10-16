import cv2
import cv2 as cv

img1 = cv2.imread("myg.png")
img2 = cv2.imread("sky.jpeg")
img3 = cv2.imread("dark.jpg")

# cvtColor

hsv1 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(img2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(img3, cv.COLOR_BGR2HSV)

# calcHist

hist1 = cv.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist2 = cv.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist3 = cv.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])

# normalize

cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

# compareHist

# HISTCMP_CORREL

c1 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
c2 = cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)
c3 = cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL)


print(f"Histogram karşılaştırma sonucu (hist1, hist2): {c1}")
print(f"Histogram karşılaştırma sonucu (hist1, hist3): {c2}")
print(f"Histogram karşılaştırma sonucu (hist2, hist3): {c3}")