#!/usr/bin/env python
import httplib

#conn = httplib.HTTPConnection("www.random.org")
#conn.request("GET","/integers/?num=10&min=1&max=6&col=1&base=10&format=plain&rnd=new")

conn = httplib.HTTPConnection("www.example.org")
conn.request("GET","/index")
print dir(conn)


res = conn.getresponse()
print res.status, res.reason
data = res.read()
array = []
for num in data:
	if num != '\n':
		array.append(int(num))
	
print array
print data

conn.close()
	
