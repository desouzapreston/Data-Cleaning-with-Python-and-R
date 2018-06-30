import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# df1 = pd.read_csv('./datasets/df1',index_col = 0)
# print(df1.head())

#df2 = pd.read_csv('df2')
#print(df2.head())
# plt.show(df1['A'].hist(bins=40))

# tips = sns.load_dataset('tips')

# print(tips.head())
# plt.show(sns.pairplot(tips))
# plt.show(sns.pairplot(tips,hue='sex'))

df = pd.read_csv('911.csv')
# print(df.info())
# print(df.head())

#top 5 zipcodes
print(df['zip'].value_counts().head(5))
#this is a test of your github fool 6/30 @ 12:14pm
#2nd test
#3rd test
#4th test
