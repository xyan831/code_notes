# write csv for gacha
# xyan831

# import module
import pandas as pd

# probablilty
Type = ['SSR', ' SR', '  R', '  N']
Weight = [1, 20, 50, 29]

# pool
SSR = ['SSR_one', 'SSR_two', 'SSR_three']
SR = ['SR_one', 'SR_two', 'SR_three']
R = ['R_one', 'R_two', 'R_three']
N = ['N_one', 'N_two', 'N_three']

# create master list
mlst = [[Type[0], Weight[0], SSR],
		[Type[1], Weight[1], SR],
		[Type[2], Weight[2], R],
		[Type[3], Weight[3], N]]

# create dataframe
gacha = pd.DataFrame(mlst, columns=['Type', 'Weight', 'Gacha'])

# write to csv
gacha.to_csv(r"C:\Users\xyan8\Documents\0_program\Python Scripts\gacha_CSV.csv")
