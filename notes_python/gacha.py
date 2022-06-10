# gacha
# xyan831

# import module
import random

# pool
SSR = ['SSR_one', 'SSR_two', 'SSR_three']
_SR = ['SR_one', 'SR_two', 'SR_three']
__R = ['R_one', 'R_two', 'R_three']
__N = ['N_one', 'N_two', 'N_three']

# probablilty
Weight = [4, 20, 50, 30]

# create master list
mlst = [['SSR', SSR],
		[' SR', _SR],
		['  R', __R],
		['  N', __N]]

# pull from pool
def gachaGet(Type, Lst):
	print(f'{Type}：  {random.choice(Lst)}')

# number of pulls
def gacha(num):
	print('你抽到了：')
	gachalst = random.choices(mlst, weights=Weight, k=num)
	for i in gachalst:
		gachaGet(i[0], i[1])

# pull gacha
gacha(10)
