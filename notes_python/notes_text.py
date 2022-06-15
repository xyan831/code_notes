# notes_text
# xyan831

# import module
import os
import re

# get all files from directory based on file type
def get_all_files(directory, type='.py'):
	files = []
	for file in os.listdir(directory):
		if file.endswith(type):
			files.append(file)
	return files

# rename file
def rename_file(directory, oldname, newname):
	olddir = directory+'\\'+oldname
	newdir = directory+'\\'+newname
	os.rename(olddir, newdir)

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
files = get_all_files(directory, '.txt')
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
