import requests
import urllib2
from bs4 import BeautifulSoup

done = []

while(True):
	url = "http://codeforces.com/contests"

	content = urllib2.urlopen(url).read()

	soup = BeautifulSoup(content,"html.parser")

	doc = soup.prettify()

	box = soup.find_all('div',{"class" : "roundbox sidebox"})
	index = []
	idx = 0
	for content in box:
		link = content.find_all('a')
		time = content.find_all('span',{"class" : "countdown"})
		# for a in link:
			# print a.get_text()
		for t in time:
			# print t.get_text()
			tleft = t.get_text()
			upper = "12:00:00"
			if any(link[2*idx].get_text() in s for s in done):
				continue
			if(tleft <= upper):
				done.append(link[2*idx].get_text())
				index.append(idx)
				print "http://codeforces.com"+link[2*idx+1].get('href')
				print t.get_text()
			idx += 1