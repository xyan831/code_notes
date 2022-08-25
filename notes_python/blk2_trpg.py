# trpg
# xyan831

# import module
import random as rd

# roll dices
def roll(dice, face):
	lst = []
	for i in range(dice):
		lst.append(rd.randint(1, face))
	return sum(lst)

# roll success rate
def rollOK(rate, level=1):
	num = rd.randint(1, 100)
	if (level==1):
		name = "普通"
	elif (level==2):
		name = "困难"
		rate = int(rate/2)
	elif (level==3):
		name = "极难"
		rate = int(rate/5)
	ok = "成功" if (num<=rate) else "失败"
	if (num<=5):
		ok = "大成功"
	if (num>=96):
		ok = "大失败"	
	print(f"{name}:\t{num} / {rate}\t\t{ok}")

# roll coc character stat
class rollCOC:
	# initialize char
	def __init__(self):
		self.str = 5*roll(3,6)					# strength
		self.con = 5*roll(3,6)					# constitution
		self.siz = 5*(roll(2,6)+6)				# size
		
		self.dex = 5*roll(3,6)					# dexterity
		self.app = 5*roll(3,6)					# appearance
		self.int = 5*(roll(2,6)+6)				# intelligence
		
		self.pow = 5*roll(3,6)				 	# power
		self.edu = 5*(roll(2,6)+6)				# education
		self.luck = 5*(roll(2,6)+6)				# luck
		
		self.hp = int((self.siz+self.con)/10)	# hit point
		self.mp = int(self.pow/5)				# magic point
		self.san = self.pow						# sanity
		self.move = self.getMove()				# move rate
	# get move rate
	def getMove(self):
		if (self.dex<self.siz)and(self.str<self.siz):
			return 7
		elif (self.dex>self.siz)and(self.str>self.siz):
			return 9
		else:
			return 8
	# print stat
	def printStat(self):
		print("COC角色随机属性\n")
		print(f"生命: {self.hp}\t\t魔法: {self.mp}")
		print(f"理智: {self.san}\t\t移动: {self.move}\n")
		print(f"力量: {self.str}\t\t敏捷: {self.dex}\t\t意志: {self.pow}")
		print(f"体质: {self.con}\t\t外貌: {self.app}\t\t教育: {self.edu}")
		print(f"体型: {self.siz}\t\t智力: {self.int}\t\t幸运: {self.luck}")
