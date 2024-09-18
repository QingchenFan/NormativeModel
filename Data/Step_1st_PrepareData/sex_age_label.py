import pandas as pd
import glob
import os

path = '/Users/qingchen/Documents/Data/HCP/HCPData/HCPSchaefer400FC/'
subFile = os.listdir(path)

label = pd.read_csv('/Users/qingchen/Documents/Data/HCP/HCP1200_age_gender.csv')

idlist = label['participant_id'].tolist()

inflist = []
for i in subFile:
    if i in idlist:
        index = idlist.index(i)
        print(label.loc[index])

        inflist.append(label.loc[index])

# 将列表转换为 DataFrame
df = pd.DataFrame(inflist)

# 将 DataFrame 保存为文件
df.to_csv('./demographics_part.csv', index=False)