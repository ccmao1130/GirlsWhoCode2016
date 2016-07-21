# Obamicon
# 07/08/2016

from PIL import Image
im = Image.open("babyme.jpg")
im.show() # shows original imae
pixels = list(im.getdata()) # gets all the pixel data from original image

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

new_im = [] # new list, cannot modify color because color is a "counter", need to append color of pixel to new list so that color is not modified
for color in pixels:
	if color[0] + color[1] + color[2] < 182 : # checks for intensity of pixel
		new_im.append(darkBlue)
	elif color[0] + color[1] + color[2] >= 182 and color[0] + color[1] + color[2] < 364: # checks for intensity of pixel
		new_im.append(red)
	elif color[0] + color[1] + color[2] >= 364 and color[0] + color[1] + color[2] < 546: # checks for intensity of pixel
		new_im.append(lightBlue)
	elif color[0] + color[1] + color[2] >= 546: # checks for intensity of pixel
		new_im.append(yellow)

new_shib = Image.new("RGB", im.size) # creates new "blank" image
new_shib.putdata(new_im) # puts data from new list of (modified) pixels into the image
new_shib.show() # shows new image