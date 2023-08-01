import cv2
import tkinter
from tkinter import messagebox



#parameters
src="20220127000305_IMG_0925.JPG"
re_img="BhuwanKhatiwada(Resized).png"
scale_percent = 60  # percent of original size

#Reading and showing original image
img= cv2.imread(src, cv2.IMREAD_UNCHANGED)
cv2.imshow("Bhuwan Khatiwada", img)

messagebox.showinfo("Diresction","Press 'ok' to see resized image")
#cv2.waitKey(0)

print('Original Dimensions : ', img.shape)


#Calculation of resized dimensions
re_width = int(img.shape[1] * scale_percent / 100)
re_height = int(img.shape[0] * scale_percent / 100)
dim = (re_width, re_height)

# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

cv2.imshow("Resized image", resized)

cv2.imwrite(re_img, resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

