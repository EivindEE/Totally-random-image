#!/usr/bin/env python
import urllib2


def rgb(c):
    split = (c[0:2], c[2:4], c[4:6])
    return [int(x, 16) for x in split]

def randint(num):
	request = urllib2.Request('http://www.random.org/integers/?num={0}&min=0&max=16777215&col=1&base=16&format=plain&rnd=new'.format(num))
	request.add_header('User-Agent', 'Totally-random-image/1.0 +eivind.elseth@gmail.com')
	print request
	opener = urllib2.build_opener() 
	randstring = opener.open(request).read()

	randarray = []
	for item in randstring.split():
		if item != '\n':
			randarray.append(rgb(item))
	
	return randarray

	