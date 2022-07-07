# notes_text
# xyan831

# import module
import os
import re

class File:
	# get all files from directory based on file type
	def TYPE(filetyp='.py', filedir=os.getcwd()):
		filelst = []
		for file in os.listdir(filedir):
			if file.endswith(filetyp):
				filelst.append(file)
		return filelst
	def RENAME(oldname, newname, directory=os.getcwd()):
		olddir = directory+'\\'+oldname
		newdir = directory+'\\'+newname
		os.rename(olddir, newdir)
	def REMOVE(lst, filedir=os.getcwd()):
		for i in lst:
			os.remove(filedir+'\\'+i)

class Text:
	def FIND(mark, txt):
		pat = re.compile(mark[0]+'(.*?)'+mark[1], re.S)
		lst = pat.findall(txt)
		return lst
	def DEL(lst, txt):
		for item in lst:
			txt = txt.replace(item, '')
		return txt

# test
filelst = File.TYPE()
print(filelst)

text1 = 'asdf=5;iwantthis123jasd asdf=5;iwantthis123jasd'
mark = ['asdf=5;', '123jasd']
txtlst = Text.FIND(mark, text1)
print(txtlst)

chara = [' ', '\n', '\t']
text2 = 'yo wasupo \n \t sfdgsdfg'
text = Text.DEL(chara, text2)
print(text)
