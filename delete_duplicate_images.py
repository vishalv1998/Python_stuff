from PIL import Image
import imagehash
import os
import time
def compare_and_delete_duplicates():
	path=input("Enter the directory inside RedditPics: ")
	path="/home/vishal/RedditPics/"+path+"/"
	try:
		os.chdir(path)
	except:
		print("directory does not exist")
		return
	x=os.listdir()
	to_be_deleted={}
	for image in range(len(x)):
		#print(x[image])
		#time.sleep(5)
		to_be_deleted[str(x[image])]=str(imagehash.average_hash(Image.open(x[image])))
	duplicates={}
	for key,value in to_be_deleted.items():
		if value not in duplicates.values():
			duplicates[key]=value
	for f in x:
		if f not in duplicates.keys():
			os.remove(f)
compare_and_delete_duplicates()