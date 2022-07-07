# gacha
# xyan831

# import module
import random

# class for gacha
class Gacha:
	def __init__(self, pool, weight):
		self.pool = pool
		self.weight = weight
	# pull gacha
	def PULL(self, num):
		# pull from pool
		def GET(Type, Lst):
			print(f'{Type}：  {random.choice(Lst)}')
		# start gacha
		print('你抽到了：')
		# choose pools
		gachalst = random.choices(self.pool, weights=self.weight, k=num)
		# pull gachas
		for i in gachalst:
			GET(i[0], i[1])

# pool
SSR = ['SSR_ein', 'SSR_zwei', 'SSR_drei']
_SR = ['SR_ein', 'SR_zwei', 'SR_drei']
__R = ['R_ein', 'R_zwei', 'R_drei']
__N = ['N_ein', 'N_zwei', 'N_drei']

# create master list
pool = [['SSR', SSR],
		[' SR', _SR],
		['  R', __R],
		['  N', __N]]

# probablilty
weight = [4, 20, 50, 30]

# pull gacha
gacha = Gacha(pool, weight)
gacha.PULL(10)
