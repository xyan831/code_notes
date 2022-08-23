# coc
# xyan831

# import module
from math import ceil
from notes_math import roll

# coc character creation
class COC:
	# initialize char
	def __init__(self, pc, pl):
		self.pc = pc							# character
		self.pl = pl							# player
		
		self.str = 5*sum(roll(3,6))				# strength
		self.con = 5*sum(roll(3,6))				# constitution
		self.siz = 5*(sum(roll(2,6))+6)			# size
		
		self.dex = 5*sum(roll(3,6))				# dexterity
		self.app = 5*sum(roll(3,6))				# appearance
		self.int = 5*(sum(roll(2,6))+6)			# intelligence
		
		self.pow = 5*sum(roll(3,6))			 	# power
		self.edu = 5*(sum(roll(2,6))+6)			# education
		self.luck = 5*(sum(roll(2,6))+6)		# luck
		
		self.hp = ceil((self.siz+self.con)/10)	# hit point
		self.mp = ceil(self.pow/5)				# magic point
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
	def PC(self):
		print(f"PC: {self.pc}\t\tPL: {self.pl}\n")
		print(f"生命: {self.hp}\t\t魔法: {self.mp}")
		print(f"理智: {self.san}\t\t移动: {self.move}\n")
		print(f"力量: {self.str}\t\t敏捷: {self.dex}\t\t意志: {self.pow}")
		print(f"体质: {self.con}\t\t外貌: {self.app}\t\t教育: {self.edu}")
		print(f"体型: {self.siz}\t\t智力: {self.int}\t\t幸运: {self.luck}")

'''
# test
pc = COC("微蓝", "大海")
pc.PC()
'''
