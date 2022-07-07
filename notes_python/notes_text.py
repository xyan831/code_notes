# notes_text
# xyan831

# import module
import os
import re

# class for files
class File:
	# get all files from directory based on file type
	def TYPE(filetyp='.py', filedir=os.getcwd()):
		filelst = []
		for file in os.listdir(filedir):
			if file.endswith(filetyp):
				filelst.append(file)
		return filelst
	# rename file
	def RENAME(oldname, newname, directory=os.getcwd()):
		olddir = directory+'\\'+oldname
		newdir = directory+'\\'+newname
		os.rename(olddir, newdir)
	# remove file
	def REMOVE(lst, filedir=os.getcwd()):
		for i in lst:
			os.remove(filedir+'\\'+i)

# class for text
class Text:
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
