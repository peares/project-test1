import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import erosion , dilation
from skimage.measure import label,regionprops

A = plt.imread('A.jpg')#การใส่รูปเข้ามาใน โปรแกรม
B1 = A[ : , : 2800]  > 140 #การตัดรูปโดยที่ A[ :190 , : ] แปลว่า 0ถึง190 ข้างหลังคือการปรับแสง
B2 = A[: , 2800: ] > 108
B = np.hstack((B1,B2)) #คือการรวมรูป B1 B2 ให้เป็นรูปเดียวกัน
B = erosion(B , np.ones((4,4))) #ตัวกัดรูป ลองปรับๆสองตัวหลังดู
B = dilation(B , np.ones((2,2))) #การขยายภาพ สำหรับตัวที่ถูกกัดจนจางหรือเติมตัวที่แหว่ง
L = label(B) #คือส่วนที่เป็นสีขาวของรูปB

plt.subplot(2,3,1)      #คือการปริ๊นรูปหลายๆรูป 1รูปต่อ1subplot โดยแบ่งเป็น (R/C/ตำแหน่ง)
plt.imshow(A , cmap='hsv')  #คือการเปลี่ยนสีของรูป เช่น gray จะเป็นสีเทา hsv จะเป็นภาพสี ///plt.imshow(A , cmap='hsv') A คือ รูป


plt.subplot(2,3,2)
plt.imshow(B1 , cmap='gray')

plt.subplot(2,3,3)
plt.imshow(B2 , cmap='gray')

plt.subplot(2,3,5)
plt.imshow(B , cmap='gray')



count = 0

for i in regionprops(L) : #ลูป ตัวนับ/ตัวจุดพ้อย ของโปรแกรม
    if i.area >10 : #การกำหนดขนาดพื้นที่ของจุดที่เราจะจุดลงไป โดยกำหนดจากตัวเลขที่เรากำหนด
        count = count + 1
        plt.plot(i.centroid[1], i.centroid[0], '*r') #ตัวกำหนดจุดกึ่งกลางของรูป โดย r คือสี


print("GGG",count) #โชว์ค่าที่นับได้
plt.show()