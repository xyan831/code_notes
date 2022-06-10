# gacha
# xyan831

import random

# probablilty
gachaType = ['SSR', 'SR', 'R', 'N']
gachaWeight = [4, 10, 20, 10]

# pool
SSR = ['SSR_one', 'SSR_two', 'SSR_three']
SR = ['SR_one', 'SR_two', 'SR_three']
R = ['R_one', 'R_two', 'R_three']
N = ['N_one', 'N_two', 'N_three']

# pull from pool
def gachaGet(Type, Lst):
  print(f'{Type}：  {random.choice(Lst)}')

# number of pulls
def gacha(num):
  print('你抽到了：')
  gachaLst = random.choices(gachaType, weights=gachaWeight, k=num)
  for i in gachaLst:
    if (i=='SSR'):
      gachaGet('SSR', SSR)
    elif (i=='SR'):
      gachaGet(' SR', SR)
    elif (i=='R'):
      gachaGet('  R', R)
    elif (i=='N'):
      gachaGet('  N', N)

# pull gacha
gacha(10)
