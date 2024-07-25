##This is the offical script for calculating the averages.
import pandas as pd
from scipy import stats
import numpy as np

df = pd.read_csv('./dataset/combined_layer.csv')


##an id for every block/segment in the swie walk data
LaSalle_SWID = [16464, 16677, 7378, 12257, 9362, 7849, 7307]
Colfax_SWID = [12271, 5851, 7726, 16686, 16685, 16682, 16681, 7306, 7033, 7032, 7207]

LaSalle_df = df[df['SW ID'].isin(LaSalle_SWID)]
Colfax_df = df[df['SW ID'].isin(Colfax_SWID)]

average_lasalle = LaSalle_df['Stress score'].mean()
average_colfax = Colfax_df['Stress score'].mean()

print(f"The average stress score of lasalle is: {average_lasalle}")
print(f"The average stress score of colfax is: {average_colfax}")

lasalle_std = LaSalle_df['Stress score'].std()
colfax_std = Colfax_df['Stress score'].std()
print(f'lasalle: {lasalle_std}')
print(f'colfax:{colfax_std}')

ttest = stats.ttest_1samp(LaSalle_df['Stress score'], Colfax_df['Stress score'].mean())
print(f'overall t-test between colfax and lasalle: {ttest}')

ttest_result = stats.ttest_ind(LaSalle_df['Stress score'], Colfax_df['Stress score'])
statistic = round(ttest_result.statistic, 2)
pvalue = ttest_result.pvalue
formatted_pvalue = f"{pvalue:.2e}" if pvalue < 0.01 else f"{pvalue:.2f}"
df = len(LaSalle_df) + len(Colfax_df) - 2
print(f"Overall t-test between Colfax and LaSalle:")
print(f"Statistic: {statistic}, p-value: {formatted_pvalue}, degrees of freedom: {df}")