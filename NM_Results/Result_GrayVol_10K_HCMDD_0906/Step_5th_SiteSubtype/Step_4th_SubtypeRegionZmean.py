import pandas as pd

alldata = pd.read_csv('./step2_group_subtype1.csv', index_col=0)

data=alldata.iloc[:,1:]
column_means = data.mean()


print(column_means)
df = pd.DataFrame(column_means)

df.to_csv('./step4_group_subtype1_Regionmean.csv')

