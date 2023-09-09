from imagecorruptions import corrupt 
import glob
import cv2
import matplotlib.pyplot as plt
import os

x = ["shot_noise", "impulse_noise", "glass_blur", "motion_blur", "snow", "frost", "elastic_transform","pixelate"]
data = "/home/akugyo/Downloads/mirflickr/*"

for images in glob.glob(data):
	for j in range(len(x)):
		i = cv2.imread(images)
		cor = corrupt(i,corruption_name=x[j],severity=2)
		cv2.imwrite("/home/akugyo/images/"+str(j)+os.path.basename(images),cor)
		print(images)