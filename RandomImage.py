#!/usr/bin/env python
from PIL import Image
import random
import argparse

parser = argparse.ArgumentParser(description='Creates a totally random image, optionaly with a size.')
parser.add_argument("--width", type=int, help='the width of the image')
parser.add_argument("--height", type=int, help='the height of the image')

args = parser.parse_args()
if args.width:
	x = args.width
else:
	x = random.randint(1, 2000)
if args.height:
	y = args.height
else:
	y = random.randint(1, 2000)

im = Image.new("RGB", (x,y), "green")

for i in range(0,x):
	for j in range(0,y):
		im.putpixel((i,j), ((random.randint(0,255),random.randint(0,255), random.randint(0,255))))

	
im.show()