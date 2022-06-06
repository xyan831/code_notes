# notes_text

# import module
import os
import re

# get all files from directory based on file type
def get_all_files(directory, type=".py"):
	# initializing empty file paths list
	files = []
	# crawling through directory
	for file in os.listdir(directory):
		#checks file type
		if file.endswith(type):
			files.append(file)
	return files

# find text
def find(word1, word2, txt):
	pat = re.compile(word1+'(.*?)'+word2, re.S)
	lst = pat.findall(txt)
	return lst

# delete characters
def delchar(lst, txt):
	line = txt
	for item in lst:
		line = line.replace(item, '')
	return line

# test
directory = r"C:\Users\xyan8\Documents\0_program\Python Scripts"
files = get_all_files(directory)
print(files)

s = 'asdf=5;iwantthis123jasd asdf=5;iwantthis123jasd'
w1 = 'asdf=5;'
w2 = '123jasd'
ln = find(w1, w2, s)
print(ln)

cd = [' ', '\n', '\t']
text = 'yo wasupo \n \t sfdgsdfg'
lin = delchar(cd, text)
print(lin)
