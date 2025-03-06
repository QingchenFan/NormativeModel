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
# 假设有两组数据
hc = pd.read_csv(
    '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/Longitudinal/Medication/First_8w_resp_0wNum.csv', index_col=0)
data = list(hc['outliers_counts'])


asd1 = pd.read_csv(
    '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/Longitudinal/Medication/Medication_8w_First_noresp_GreaterOrLess_1.96num.csv', index_col=0)
data1 = list(asd1['outliers_counts'])

asd = pd.read_csv(
    '/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1228-2024122801_test/Step_5th_Subtype/step5_subtype2_GreaterOrLess_RegionNum_1.96num.csv', index_col=0)
data2 = list(asd['outliers_counts'])



df = pd.DataFrame({
    'Group': ['HCs'] * len(data) + ['Subtype1'] * len(data1) + ['Subtype2'] * len(data2),
    'Values': data + data1 + data2
})


# 绘制小提琴图
fig, ax = plt.subplots()
palette = {'HCs': '#8BACD1', 'Subtype1': '#C17F9E', 'Subtype2': '#80B1D3'}  # 修改Subtype2的颜色以区分
sns.violinplot(x='Group', y='Values', data=df, ax=ax, palette=palette)

# 设置y轴限制
y_max = df['Values'].max()
plt.ylim(0, y_max)

# 设置y轴标签和其他图形属性
ax.set_ylabel('Num of Extreme Deviation')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks(range(len(df['Group'].unique())))
ax.set_xticklabels(df['Group'].unique())

# 两两t检验并添加注释
alpha = 0.05
group_names = df['Group'].unique()
group_indices = {name: idx for idx, name in enumerate(group_names)}
pvaluebox = []
for i in range(len(group_names)):
    for j in range(i + 1, len(group_names)):
        group1 = group_names[i]
        group2 = group_names[j]
        group1_data = df[df['Group'] == group1]['Values']
        group2_data = df[df['Group'] == group2]['Values']

        t_stat, p_value = ttest_ind(group1_data, group2_data)
        cond = cohen_d(group1_data,group2_data)
        print(f'p value between {group1} and {group2} - pvalue： ', p_value, ' cohen-d：', cond)
        pvaluebox.append(p_value)
        if p_value < alpha:
            # 计算注释位置
            x_pos = (group_indices[group1] + group_indices[group2]) / 2
            x1 = group_indices[group1]
            x2 = group_indices[group2]
            # ax.plot([x1, x2], [y_max , y_max], '-', color='black', linewidth=0.5)
            # ax.text(x_pos, y_max - 2.2, '*', fontsize=12, ha='center', va='bottom', color='black')

        # 保存并显示图表
rejected, fdr_pvalue, _, _ = smm.multipletests(pvaluebox, alpha=0.05, method='fdr_bh')
print(fdr_pvalue)
plt.savefig('./step6_1_NumberOfExtremeDeviation.png', dpi=300)
plt.show()