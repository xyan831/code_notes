# gacha
# xyan831

# import module
import random

# class for gacha
class Gacha:
	def __init__(self, pool, weight):
		self.pool = pool
		self.weight = weight
		self.own = {}
	# pull gacha
	def PULL(self, num):
		# start gacha
		print('你抽到了：')
		# choose pools
		gachalst = random.choices(self.pool, weights=self.weight, k=num)
		# pull from pool
		for i in gachalst:
			char = random.choice(i[1])
			print(f"{i[0]}：  {char}")
			if (char in self.own):
				self.own[char] += 1
			else:
				self.own[char] = 1
'''
# pool
ssr = ['SSR_ein', 'SSR_zwei', 'SSR_drei']
sr = ['SR_ein', 'SR_zwei', 'SR_drei']
r = ['R_ein', 'R_zwei', 'R_drei']
n = ['N_ein', 'N_zwei', 'N_drei']

# create pool list
pool = [['SSR', ssr],
		[' SR', sr],
		['  R', r],
		['  N', n]]

# probablilty
weight = [4, 20, 50, 30]

# pull gacha
gacha = Gacha(pool, weight)
gacha.PULL(10)
'''
