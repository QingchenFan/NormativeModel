import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import pandas as pd
import numpy as np
import statsmodels.stats.multitest as smm
def cohen_d(group1, group2):
    """
    计算Cohen's d
    :param group1: 第一组数据（一维数组或列表）
    :param group2: 第二组数据（一维数组或列表）
    :return: Cohen's d值
    """
    n1, n2 = len(group1), len(group2)
    mean1, mean2 = np.mean(group1), np.mean(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    return (mean1 - mean2) / pooled_std
'''
    被试水平 统计一个被试 大于1.96或小于-1.96 的脑区数量总和 将其画小提琴图  。比较了HC MDD 异常脑区数量的差异
'''
# 假设有两组数据
hc = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/Longitudinal/Medication/w8/SSRI/subtype_2_Z_AllMDD_GreaterOrLess_1.96num.csv')
data1 = list(hc['outliers_counts'])

mdd = pd.read_csv(
    '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/Longitudinal/Medication/w8/SSRI/subtype2_SSRI_m8w_Z8w_GreaterOrLess_1.96num.csv')
data2 = list(mdd['outliers_counts'])

# 创建一个DataFrame来存储数据
df = pd.DataFrame({'Group': ['subtype2-8w'] * len(data2) + ['subtype2-0w'] * len(data1), 'Values': data2 + data1})

# 创建图形和轴对象
fig, ax = plt.subplots()

# 设置不同的颜色给两个分组
palette = {'subtype2-8w': '#C17F9E', 'subtype2-0w': '#8BACD1'}

# 绘制小提琴图，并使用不同的颜色
sns.violinplot(x='Group', y='Values', data=df, ax=ax, palette=palette)

# 进行统计测试（这里使用双样本t检验）
t_stat, p_value = ttest_ind(data1, data2)
cohend = cohen_d(data1, data2)
# 根据p值决定是否添加星星
alpha = 0.05
print('cohend - ', cohend)
print('p value - ', p_value)
print('t value - ', t_stat)
if p_value < alpha:
    # 计算横线位置
    x_min, x_max = ax.get_xlim()
    y_max = ax.get_ylim()[1]
   # ax.axhline(y=y_max - 2.2, xmin= 0.25, xmax=0.75, color='gray', linestyle='-', linewidth=1)
    ax.text((x_min + x_max) / 2, y_max - 2.2, '*', fontsize=12, ha='center', va='bottom', color='black')

# 设置y轴从0开始
y_max = max(max(data1), max(data2))
plt.ylim(0, y_max)
# 设置y轴的标签
ax.set_ylabel('Number of Extreme Deviation')
# 去掉上边框和右边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 确保横坐标刻度线与分类标签对齐
ax.set_xticks(range(len(df['Group'].unique())))
ax.set_xticklabels(df['Group'].unique())
plt.savefig('./subtype2_NumberofExtremeDeviation.png', dpi=300)
# 显示图表
plt.show()
