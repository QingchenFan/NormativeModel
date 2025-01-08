import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import pandas as pd
import seaborn as sns
import numpy as np
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
#negative
'''
    被试水平 统计一个被试小于-1.96 的Z值之和 将其画小提琴图。比较了HC MDD Negative脑区Z值之和的差异
'''
# 假设有两组数据
hc = pd.read_csv(
    '/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1228-2024122801/Step_3th_OutliersCount/Step2_Z_AllHCestimate_LessThan_-196sum.csv', index_col=0)
data1 = list(hc['sum_196'])
print(data1)
mdd = pd.read_csv('/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1228-2024122801/Step_3th_OutliersCount/Step2_Z_AllMDD_LessThan_-196sum.csv', index_col=0)
data2 = list(mdd['sum_196'])
print(data2)
# 创建一个DataFrame来存储数据
df = pd.DataFrame({'Group': ['MDD'] * len(data2) + ['HCs'] * len(data1), 'Values': data2 + data1})

# 创建图形和轴对象
fig, ax = plt.subplots()

# 设置不同的颜色给两个分组
palette = {'MDD': '#C17F9E', 'HCs': '#8BACD1'}

# 绘制小提琴图，并使用不同的颜色
sns.violinplot(x='Group', y='Values', data=df, ax=ax, palette=palette)

# 进行统计测试（这里使用双样本t检验）
t_stat, p_value = ttest_ind(data1, data2)
cohend = cohen_d(data2, data1)
print('cohend - ',cohend)
print('p value - ',p_value)
print('t value - ',t_stat)
y_min = df['Values'].min()  # 获取整个数据集的最大值

plt.ylim(y_min, 0)
custom_yticks = [0, -40, -80, -120, -160]
plt.yticks(custom_yticks)

# 根据p值决定是否添加星星
alpha = 0.05
if p_value < alpha:
    # 计算横线位置
    x_min, x_max = ax.get_xlim()
    y_max = ax.get_ylim()[1]
   # ax.axhline(y=y_max - 2.2, xmin= 0.25, xmax=0.75, color='gray', linestyle='-', linewidth=1)
    ax.text((x_min + x_max) / 2, y_max - 2.2, '***', fontsize=12, ha='center', va='bottom', color='black')

# 设置y轴从0开始
y_max = max(max(data1), max(data2))
# plt.ylim(0, y_max)
# 设置y轴的标签
ax.set_ylabel('Sum of Negative Deviation')
# 去掉上边框和右边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 去除刻度线 设置轴上数字大小
plt.gca().tick_params(axis='x', which='both', width=0, labelsize=12)
plt.gca().tick_params(axis='y', which='both', width=0, labelsize=12)

# 设置下边框和左边框的线宽
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)

# 确保横坐标刻度线与分类标签对齐
ax.set_xticks(range(len(df['Group'].unique())))
ax.set_xticklabels(df['Group'].unique())
plt.savefig('./step2_SumOfNegativeDeviation-1.96.png', dpi=300)
# 显示图表
plt.show()
