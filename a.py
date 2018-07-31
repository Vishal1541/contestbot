from facepy import GraphAPI
import time as ti
import facebook
import json
import requests
import urllib2
from bs4 import BeautifulSoup

access_token = "EAAZAcOu3MZASIBAE6LiWAujw2y3VFn9gbR0d4ZAK1W522JeysZCB2vOTXcJswZBSHZAeU8FB3DAd0abTy84ZCv6xc2xepiZBfop9oAwtbPND0ZC82ZAmzEUr5DM80uAzksJDRw83NPtbV43UZAJC462xcnKwwOZA5jMTv8RPmoOLncqBSPWuvs83FEUb1QpSJawpQtsZD"
message = ""
done = []
graph = GraphAPI(access_token)
group_id = "1764599366969836"

# 1764599366969836 dummy
# 455401031299537 kamand prompt

def createPost(posts, amount):
	for post in posts:
		url = "https://graph.facebook.com/{0}/comments".format(post['id'])
		parameters = {'access_token' : access_token, 'message' : message}
		s = requests.post(url, data = parameters)

def get_posts():
	payload = {'access_token' : access_token}
	r = requests.get('https://graph.facebook.com/me/feed', params = payload)
	result = json.loads(r.text)
	return result['data']

while(True):
	ti.sleep(5)
	url = "http://codeforces.com/contests"

	content = urllib2.urlopen(url).read()

	soup = BeautifulSoup(content,"html.parser")

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
			upper = "24:00:00"
			if any(link[2*idx].get_text() in s for s in done):
				continue
			if(tleft <= upper):
				done.append(link[2*idx].get_text())
				index.append(idx)
				title = "**CONTEST REMINDER**\n";
				contest_name = "Contest Name: "+link[2*idx].get_text()+"\n";
				contest_link = "Contets Link: http://codeforces.com"+link[2*idx+1].get('href')+"\n";
				time_left = t.get_text()[0]+t.get_text()[1]+" hours "+t.get_text()[3]+t.get_text()[4]+" minutes left\n"
				rgds = "Happy Coding :)\n"
				message = title+contest_name+contest_link+time_left+rgds;
				print message
				graph.post(path = (group_id) + '/feed', message = message)
			idx += 1