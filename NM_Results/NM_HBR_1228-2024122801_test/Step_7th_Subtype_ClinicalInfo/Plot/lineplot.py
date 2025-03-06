import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取CSV文件
data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/PLSC/subtype1_HAMD_explCovLC.csv', header=None)
df_top10 = data.head(10)

# 设置索引
df_top10.index = range(1, 11)
print(df_top10)

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制散点图（圆点）
sns.scatterplot(x=df_top10.index, y=0, data=df_top10, s=100, color='#78A9D1', marker='o')

# 设置x轴和y轴刻度
ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 去掉上面和右边的线条
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 自定义x轴和y轴的线条粗细
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

# 去掉x轴和y轴上的小刻度线
ax.tick_params(axis='both', which='both', labelsize=12, bottom=False, top=False, left=False, right=False)

# 设置图表标题和坐标轴标签
ax.set_xlabel('PLS Component', size=14)
ax.set_ylabel('Explained variance', size=14)

# 显示图形
plt.show()
