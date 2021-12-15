import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import erosion , dilation
from skimage.measure import label,regionprops

A = plt.imread('A.jpg')
A = cv2.cvtColor(A, cv2.COLOR_BGR2GRAY )
B1 = A[ : , :2800 ] >90
B2 = A[: , 2800: ] > 60
B = np.hstack((B1,B2))
B = erosion(B , np.ones((20,20)))
B = dilation(B , np.ones((5,4)))
L = label(B)

plt.subplot(2,3,1)
plt.imshow(A , cmap='gray')
plt.subplot(2,3,2)
plt.imshow(B , cmap='gray')
plt.subplot(2,3,3)
plt.imshow(B1 , cmap='gray')
plt.subplot(2,3,4)
plt.imshow(B2 , cmap='gray')
plt.subplot(2,3,5)
plt.imshow(B , cmap='gray')

count = 0

for i in regionprops(L) : #ลูป ตัวนับ/ตัวจุดพ้อย ของโปรแกรม
    if i.area >20 : #การกำหนดขนาดพื้นที่ของจุดที่เราจะจุดลงไป โดยกำหนดจากตัวเลขที่เรากำหนด
        count = count + 1
        plt.plot(i.centroid[1], i.centroid[0], '*r')

print("SUM",count)
plt.show()