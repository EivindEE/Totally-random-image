#!/usr/bin/env python
from PIL import Image
import random
import argparse
from RandomNumbers import randint

parser = argparse.ArgumentParser(description='Creates a totally random image, optionaly with a size.')
parser.add_argument("-x", "--width", type=int, help='the width of the image')
parser.add_argument("-y", "--height", type=int, help='the height of the image')

args = parser.parse_args()
if args.width:
	x = args.width
else:
	x = random.randint(1, 200)
if args.height:
	y = args.height
else:
	y = random.randint(1, 200)

num = x*y
randarray = randint(num)
im = Image.new("RGB", (x,y), "green")
for i in range(0,x):
	for j in range(0,y):
		pixel = randarray[(i*y)+j]
		im.putpixel((i,j), (pixel[0],pixel[1],pixel[2]))

	
im.show()