#!/usr/bin/env python
from PIL import Image
import random

x = 512
y = 512

im = Image.new("RGB", (x,y), "green")

for i in range(0,x):
	for j in range(0,y):
		im.putpixel((i,j), ((random.randint(0,255),random.randint(0,255), random.randint(0,255))))

	
im.show()