# notes_text
# xyan831

# import module
import os
import re

# get all files from directory based on file type
def file_typget(filetyp='.py', filedir=os.getcwd()):
	filelst = []
	for file in os.listdir(filedir):
		if file.endswith(filetyp):
			filelst.append(file)
	return filelst

# rename file
def file_rename(oldname, newname, directory=os.getcwd()):
	olddir = directory+'\\'+oldname
	newdir = directory+'\\'+newname
	os.rename(olddir, newdir)

# find text between 2 marks [start, end]
def find(mark, txt):
	pat = re.compile(mark[0]+'(.*?)'+mark[1], re.S)
	lst = pat.findall(txt)
	return lst

# delete characters
def delchar(lst, txt):
	for item in lst:
		txt = txt.replace(item, '')
	return txt

# test
filelst = file_typget('.txt')
print(filelst)

text1 = 'asdf=5;iwantthis123jasd asdf=5;iwantthis123jasd'
mark = ['asdf=5;', '123jasd']
txtlst = find(mark, text1)
print(txtlst)

chara = [' ', '\n', '\t']
text2 = 'yo wasupo \n \t sfdgsdfg'
text = delchar(chara, text2)
print(text)
