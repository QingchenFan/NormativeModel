import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取CSV文件
data_subtype1 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/subtype1_Brain_Lx.csv')
data_subtype2 = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/subtype1_HAMD_Ly.csv')
x = np.array(data_subtype1)
y = np.array(data_subtype2)
# 创建一个图和两个轴对象
fig, ax = plt.subplots(figsize=(10, 6))

# 在第一个轴上绘制第一个数据集的散点回归图
sns.regplot(x=x[:, 1], y=y[:, 1],  ax=ax, scatter_kws={'color': '#78A9D1'}, line_kws={'color': '#4176B8'}, ci=None)  #


# 设置图表标题和坐标轴标签
#ax.set_title('Scatter Regression Plot of Age vs Outliers Counts')
ax.set_xlabel('Brain PLS score', size=14)
ax.set_ylabel('HAMD PLS score', size=14)

# 自定义x轴和y轴的刻度

ax.set_xticks([-12, -8, -4,  0, 4, 8])  # 注意这里是set_xticks，因为你想要设置的是x轴的刻度
#ax.set_yticks([10,  30,  50,  70])
# 自定义x轴和y轴的线条粗细
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

# 去掉x轴和y轴上的小刻度线
ax.tick_params(axis='both', which='both', labelsize=12, bottom=False, top=False, left=False, right=False)

# 去掉上边线和右边线
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 显示图表
plt.show()