import cv2
import numpy as np 
import matplotlib.pyplot as plt 
# from PIL import Image

def most_frequent_colour(image):
	# image = cv2.imread('~/Desktop/3-1/DIP/asg_1/DIP_2019_A1/fg.jpg')
	w, h = image.shape()
	
	# h = np.size(image, 0)
	# w = np.size(image, 1)
	pixels = image.getcolors(w * h)
	most_frequent_pixel = pixels[0]
	for count, colour in pixels:
		if count > most_frequent_pixel[0]:
			most_frequent_pixel = (count, colour)

	compare("Most Common", image, most_frequent_pixel[1])
	return most_frequent_pixel[1]
# image = Image.open("~/Desktop/3-1/DIP/asg_1/DIP_2019_A1/fg.jpg")
image = cv2.imread('~/Desktop/3-1/DIP/asg_1/DIP_2019_A1/fg.jpg')
p = most_frequent_colour(image)
print(p)