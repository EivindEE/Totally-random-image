#!/usr/bin/env python
import httplib
import urllib2


def randint(num):
	httplib.HTTPConnection.debuglevel = 1  
	request = urllib2.Request('http://www.random.org/integers/?num={0}&min=0&max=255&col=1&base=10&format=plain&rnd=new'.format(num))
	request.add_header('User-Agent', 'Totally-random-image/1.0 +eivind.elseth@gmail.com')
	opener = urllib2.build_opener() 
	randstring = opener.open(request).read()

	randarray = []
	for item in randstring.split():
		if item != '\n':
			randarray.append(int(item))
	
	return randarray