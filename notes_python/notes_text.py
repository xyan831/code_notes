# notes_text
# xyan831

# import module
import os
import re

# file functions

# get files from directory based on file type
def getFiles(typlst, directory):
	filelst = []
	for file in os.listdir(directory):
		for typ in typlst:
			if file.endswith(typ):
				filelst.append(file)
	return filelst

# rename file in same directory
def Rename(oldname, newname, directory):
	olddir = directory+'\\'+oldname
	newdir = directory+'\\'+newname
	os.rename(olddir, newdir)

# remove files from same directory
def Remove(lst, directory):
	for i in lst:
		os.remove(directory+'\\'+i)

# clean out directory
def cleanout(directory):
	files = os.listdir(directory)
	for item in files:
		if ('.' not in item):
			cleanout(directory+'\\'+item)
			os.rmdir(directory+'\\'+item)
		else:
			os.remove(directory+'\\'+item)	

# text functions

# find text between 2 markers
def FIND(mark, txt):
	pat = re.compile(mark[0]+'(.*?)'+mark[1], re.S)
	lst = pat.findall(txt)
	return lst

# delete characters in text
def DEL(lst, txt):
	for item in lst:
		txt = txt.replace(item, '')
	return txt
