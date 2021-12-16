import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = plt.imread("results/test_1.tif")
img2 = plt.imread("dataset/test/A/test_1.png")
img3 = plt.imread("dataset/test/B/test_1.png")
img4 = plt.imread("dataset/test/label/test_1.png")

img5 = plt.imread("results/test_2.tif")
img6 = plt.imread("dataset/test/A/test_2.png")
img7 = plt.imread("dataset/test/B/test_2.png")
img8 = plt.imread("dataset/test/label/test_2.png")

img9 = plt.imread("results/test_3.tif")
img10 = plt.imread("dataset/test/A/test_3.png")
img11 = plt.imread("dataset/test/B/test_3.png")
img12  = plt.imread("dataset/test/label/test_3.png")

fig= plt.figure(figsize=(9,9),)

ax1 = fig.add_subplot(3,4,1)
ax1.set_title('A')
ax1.imshow(img2)
ax2 = fig.add_subplot(3,4,2)
ax2.set_title('B')
ax2.imshow(img3)
ax3 = fig.add_subplot(3,4,3)
ax3.set_title('Result')
ax3.imshow(img)
ax4 = fig.add_subplot(3,4,4)
ax4.set_title('Label')
ax4.imshow(img4)

ax5 = fig.add_subplot(3,4,5)
ax5.imshow(img6)
ax6 = fig.add_subplot(3,4,6)
ax6.imshow(img7)
ax7 = fig.add_subplot(3,4,7)
ax7.imshow(img5)
ax8 = fig.add_subplot(3,4,8)
ax8.imshow(img8)


ax9 = fig.add_subplot(3,4,9)
ax9.imshow(img10)
ax10 = fig.add_subplot(3,4,10)
ax10.imshow(img11)
ax11 = fig.add_subplot(3,4,11)
ax11.imshow(img9)
ax12 = fig.add_subplot(3,4,12)
ax12.imshow(img12)

plt.savefig('foo.png')
plt.show()
