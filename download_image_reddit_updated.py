import json
import urllib.request
import os
import time
from PIL import Image
import imagehash
input_from_user=input("Enter the subreddit: ")
request_url="https://old.reddit.com/r/"+input_from_user+"/.json"
break_loop=True
while(break_loop):
	try:
		data = urllib.request.urlopen(request_url)
		break_loop=False
	except:
		print("429. Trying again in 3 seconds")
		time.sleep(3)

response = data.read()  			#response -> json
response = json.loads(response)		#response -> dict
#response['data']['children'][x]['data']['url']
url_list=[]
count_of_posts=0
for i in response['data']['children'][count_of_posts]['data']:
	try:
		x=response['data']['children'][count_of_posts]['data']['url']
		if(x.endswith('.jpg')):
			url_list.append(x)
	except Exception as e:
		print("END of posts or something")
	finally:
		count_of_posts+=1


def download_image(url_list):
	name=""
	count=0
	file_name='/home/vishal/RedditPics/'+input_from_user+'/'
	#pdhsacat
	if not os.path.exists(file_name):
		os.makedirs(file_name)
	os.chdir(file_name)
	for i in url_list:
		name=input_from_user+str(count)+".jpg"
		while(name in os.listdir()):
			count+=1
			name=input_from_user+str(count)+".jpg"
		urllib.request.urlretrieve(i,name)
download_image(url_list)
#compare_and_delete_duplicates()
