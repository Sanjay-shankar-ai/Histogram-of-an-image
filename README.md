# Histogram and Histogram Equalization of an image
## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import cv2, matplotlib.py libraries and display the saved images using cv2.imshow().

### Step2:
Use cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]]) to find the histogram of the image.

### Step3:
Plot the image and its stem plots using the plt.show() and plt.stem() functions.

### Step4:
Equalize the grayscale image using the in-built function cv2.equalizeHist().

### Step5:
Print the original and equalized image using cv2.imshow() and end the program.

## Program:
```
# Developed By: Sanjay S
# Register Number: 212221230086
```
# Write your code to find the histogram of gray scale image and color image channels.
```
import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread("outer1.png")
clr_image = cv2.imread("color.jpg",-1)
cv2.imshow("Gray Image",gray_image)
cv2.imshow("Colour Image",clr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

# Display the histogram of gray scale image and any one channel histogram from color image
```
import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread("outer1.png")
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
```


# Write the code to perform histogram equalization of the image. 
```
import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread("outer1.png",0)
cv2.imshow("Gray Image",gray_image)
equ = cv2.equalizeHist(gray_image)
cv2.imshow("Equalized Image",equ)
cv2.waitKey(0)
cv2.destroyAllWindows()


```
## Output:
### Input Grayscale Image and Color Image
![Screenshot (30)](https://user-images.githubusercontent.com/94231938/230161540-851ee34f-3161-4b3a-ae23-781f682ca98b.png)

### Histogram of Grayscale Image and any channel of Color Image
![Ex4](https://user-images.githubusercontent.com/94231938/230161690-d31a9cbc-a31f-40f0-91d4-7767d7d51698.png)
![Screenshot (28)](https://user-images.githubusercontent.com/94231938/230161736-52e718d0-43b0-4e1e-bac2-ff48452a7dcb.png)
![Screenshot (27)](https://user-images.githubusercontent.com/94231938/230161894-7a2d483f-8291-47a9-82e6-483a0085cadb.png)


### Histogram Equalization of Grayscale Image
![Screenshot (29)](https://user-images.githubusercontent.com/94231938/230161943-bcd5dbe6-e081-4591-aaee-6c53bcc8d223.png)

## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.
