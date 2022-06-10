# write csv for gacha
# xyan831

# import module
import pandas as pd

# pool
SSR = ['SSR_one', 'SSR_two', 'SSR_three']
_SR = ['SR_one', 'SR_two', 'SR_three']
__R = ['R_one', 'R_two', 'R_three']
__N= ['N_one', 'N_two', 'N_three']

# probablilty
Weight = [1, 20, 50, 29]

# create master list
mlst = [['SSR', Weight[0], SSR],
		[' SR', Weight[1], _SR],
		['  R', Weight[2], __R],
		['  N', Weight[3], __N]]

# create dataframe
gacha = pd.DataFrame(mlst, columns=['Type', 'Weight', 'Gacha'])

# write to csv
gacha.to_csv(r"C:\Users\xyan8\Documents\0_program\Python Scripts\gacha_CSV.csv")
