# load gacha from csv
# xyan831

# import module
import pandas as pd
import random

# convert string to list
def strlst(lst):
	char = [r"'", ' ', '[', ']']
	for i in char:
		lst = lst.replace(i, '')
	return lst.split(',')

# pull from pool
def gachaGet(Type, Lst):
  print(f'{Type}：  {random.choice(Lst)}')

# number of pulls
def gachapull(num):
	print('你抽到了：')
	gachalst = random.choices(gacha['Type'], weights=gacha['Weight'], k=num)
	for i in gachalst:
		lst = gacha['Gacha'].where(gacha['Type']==i).dropna().values[0]
		gachaGet(i, strlst(lst))

# get dataframe from csv
gacha = pd.read_csv(r"C:\Users\xyan8\Documents\0_program\Python Scripts\gacha_CSV.csv")

# pull gacha
gachapull(10)
