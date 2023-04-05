import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread("outer1.png")
clr_image = cv2.imread("color.png",-1)
cv2.imshow("Gray Image",gray_image)
cv2.imshow("Colour Image",clr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread("outer.png")
clr_image = cv2.imread("color.jpg",-1)
gray_hist = cv2.calcHist([gray_image],[0],None,[256],[0,256])
clr_hist = cv2.calcHist([clr_image],[0],None,[256],[0,256])
plt.figure()
plt.imshow(gray_image)
plt.show()
plt.title("Histogram")
plt.xlabel("Grayscale Value")
plt.ylabel("Pixel Count")
plt.stem(gray_hist)
plt.show()
plt.imshow(clr_image)
plt.show()
plt.title("Histogram of Color Image - Green Channel")
plt.xlabel("Intensity Value")
plt.ylabel("Pixel Count")
plt.stem(clr_hist)
plt.show()

import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread("outer.png",0)
cv2.imshow("Gray Image",gray_image)
equ = cv2.equalizeHist(gray_image)
cv2.imshow("Equalized Image",equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
