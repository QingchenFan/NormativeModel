import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # 读取三个CSV文件
# df1 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/duilie_s1s2.csv')
# df2 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/Data135_s1s2.csv')
# df3 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/BrainPro_PD_s1s2.csv')
#

# import pandas as pd
# import matplotlib.pyplot as plt
#
# # 读取两个CSV文件
# df1 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/Data135_s1s2.csv')
# df2 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/Data135_s1s2.csv')
#
#
# # 分别计算df1和df2中type列中1和2的比例
# type_counts_df1 = df1['type'].value_counts(normalize=True)
# type_counts_df2 = df2['type'].value_counts(normalize=True)
#
# # 获取1和2的比例
# proportions_df1 = [type_counts_df1.get(1, 0), type_counts_df1.get(2, 0)]
# proportions_df2 = [type_counts_df2.get(1, 0), type_counts_df2.get(2, 0)]
#
# # 设置x轴的位置
# index = [0, 1]  # 代表两个柱子的位置
#
# # 绘制柱状图
# fig, ax = plt.subplots()
#
# # 绘制两个柱子，柱子分为两部分，一部分表示1的比例，另一部分表示2的比例
# ax.bar(index[0], proportions_df1[0], label='1 in BrainPro_NP_s1s2', color='skyblue')
# ax.bar(index[0], proportions_df1[1], bottom=proportions_df1[0], label='2 in BrainPro_NP_s1s2', color='orange')
#
# ax.bar(index[1], proportions_df2[0], label='1 in Data135_s1s2', color='lightgreen')
# ax.bar(index[1], proportions_df2[1], bottom=proportions_df2[0], label='2 in Data135_s1s2', color='lightcoral')
#
# # 设置标签和标题
# ax.set_xlabel('Datasets')
# ax.set_ylabel('Proportion')
# ax.set_title('Proportion of Type 1 and Type 2 in Two Datasets')
# ax.set_xticks(index)
# ax.set_xticklabels(['BrainPro_NP_s1s2', 'Data135_s1s2'])
#
# # 添加图例
# #ax.legend()
#
# # 显示图表
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/duilie_s1s2.csv')
df2 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/Data135_s1s2.csv')
df3 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/BrainPro_PD_s1s2.csv')
df4 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/BrainPro_NP_s1s2.csv')
# # 读取四个CSV文件
# df1 = pd.read_csv('BrainPro_NP_s1s2.csv')
# df2 = pd.read_csv('Data135_s1s2.csv')
# df3 = pd.read_csv('your_third_file.csv')  # 第三个表格
# df4 = pd.read_csv('your_fourth_file.csv')  # 第四个表格

# 分别计算每个表中type列中1和2的比例
type_counts_df1 = df1['type'].value_counts(normalize=True)
type_counts_df2 = df2['type'].value_counts(normalize=True)
type_counts_df3 = df3['type'].value_counts(normalize=True)
type_counts_df4 = df4['type'].value_counts(normalize=True)

# 获取每个表中1和2的比例
proportions_df1 = [type_counts_df1.get(1, 0), type_counts_df1.get(2, 0)]
proportions_df2 = [type_counts_df2.get(1, 0), type_counts_df2.get(2, 0)]
proportions_df3 = [type_counts_df3.get(1, 0), type_counts_df3.get(2, 0)]
proportions_df4 = [type_counts_df4.get(1, 0), type_counts_df4.get(2, 0)]


print(proportions_df1)
print(proportions_df2)
print(proportions_df3)
print(proportions_df4)

# 设置x轴的位置，分别代表四个柱子的位置
index = [0, 1, 2, 3]

# 绘制柱状图
fig, ax = plt.subplots()

# 绘制四个柱子，每个柱子分为两部分，一部分表示1的比例，另一部分表示2的比例
ax.bar(index[0], proportions_df1[0], label='1 in BrainPro_NP_s1s2', color='#000000')
ax.bar(index[0], proportions_df1[1], bottom=proportions_df1[0], label='2 in BrainPro_NP_s1s2', color='#F50303')

ax.bar(index[1], proportions_df2[0], label='1 in Data135_s1s2', color='lightgreen')
ax.bar(index[1], proportions_df2[1], bottom=proportions_df2[0], label='2 in Data135_s1s2', color='lightcoral')

ax.bar(index[2], proportions_df3[0], label='1 in Third Dataset', color='lightblue')
ax.bar(index[2], proportions_df3[1], bottom=proportions_df3[0], label='2 in Third Dataset', color='yellow')

ax.bar(index[3], proportions_df4[0], label='1 in Fourth Dataset', color='pink')
ax.bar(index[3], proportions_df4[1], bottom=proportions_df4[0], label='2 in Fourth Dataset', color='purple')

# 设置标签和标题
ax.set_xlabel('Datasets')
ax.set_ylabel('Proportion')
ax.set_title('Proportion of Type 1 and Type 2 in Four Datasets')
ax.set_xticks(index)
ax.set_xticklabels(['BrainPro_NP_s1s2', 'Data135_s1s2', 'Third Dataset', 'Fourth Dataset'])

# 添加图例
#ax.legend()

# 显示图表
plt.show()
