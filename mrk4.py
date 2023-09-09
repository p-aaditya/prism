import numpy as np 
#import matplotlib.pyplot as plt
from PIL import Image
import random
import cv2
import glob
import os

data1 = "/home/akugyo/Downloads/mirflickr/*"

def fun(data):
	h,w,channels=data.shape
	print(data.shape)
	x = random.randint(1, 4)
	print(x)
	y=random.randint(2,h//2)
	z=random.randint(h//2,h)
	top=y
	left=y

	#b=he//2
	bottom=z
	#r=wi//2
	right=z

	if x==1:
		img=data
		img[0:top,0:w]=(0,0,0)
		imgc=Image.fromarray(img)

	elif x==2:
		img=data
		img[0:h,0:left]=(0,0,0)
		imgc=Image.fromarray(img)
	    

	elif x==3:
		img=data
		img[bottom:h,0:w]=(0,0,0)
		imgc=Image.fromarray(img)
		

	elif x==4:
		img=data
		img[0:h,right:w]=(0,0,0)
		imgc=Image.fromarray(img)
		
	return img

for images in glob.glob(data1):
	data = cv2.imread(images)
	cor = fun(data)
	cv2.imwrite("/home/akugyo/Dataset/"+"h"+os.path.basename(images),cor)
	print(images)

