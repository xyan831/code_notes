# trpg
# xyan831

# import module
from random import randint

# roll dices
def roll(dice, face):
	lst = []
	for i in range(dice):
		lst.append(randint(1, face))
	return sum(lst)

# roll success rate
def rollOK(rate):
	num = randint(1, 100)
	if (num<=5):
		ok = "大成功"
	elif (num<=int(rate/5)):
		ok = "极难成功"
	elif (num<=int(rate/2)):
		ok = "困难成功"
	elif (num<=rate):
		ok = "成功"	
	elif (num>=96):
		ok = "大失败"
	else:
		ok = "失败"
	print(f"1d100={num}/{rate} ({ok})")

# roll coc character stat
def rollCOC():
	# roll stat
	STR = 5*roll(3,6)			# strength
	CON = 5*roll(3,6)			# constitution
	SIZ = 5*(roll(2,6)+6)		# size
	DEX = 5*roll(3,6)			# dexterity
	APP = 5*roll(3,6)			# appearance
	INT = 5*(roll(2,6)+6)		# intelligence
	POW = 5*roll(3,6)		 	# power
	EDU = 5*(roll(2,6)+6)		# education
	LUCK = 5*(roll(2,6)+6)		# luck
	# calculate stat
	HP = int((SIZ+CON)/10)		# hit point
	MP = int(POW/5)				# magic point
	SAN = POW					# sanity
	# move rate
	if (DEX<SIZ)and(STR<SIZ):
		MOVE = 7
	elif (DEX>SIZ)and(STR>SIZ):
		MOVE = 9
	else:
		MOVE = 8
	# print stat
	print("COC角色随机属性\n")
	print(f"生命: {HP}\t\t魔法: {MP}")
	print(f"理智: {SAN}\t\t移动: {MOVE}\n")
	print(f"力量: {STR}\t\t敏捷: {DEX}\t\t意志: {POW}")
	print(f"体质: {CON}\t\t外貌: {APP}\t\t教育: {EDU}")
	print(f"体型: {SIZ}\t\t智力: {INT}\t\t幸运: {LUCK}")
