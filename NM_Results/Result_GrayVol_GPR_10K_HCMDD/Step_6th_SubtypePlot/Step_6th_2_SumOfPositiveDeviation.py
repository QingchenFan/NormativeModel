import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
import pandas as pd

# 假设有两组数据
hc = pd.read_csv(
    '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_5K_HCMDD_1022/StaResults/Step2_Z_AllHCestimate_GreaterThan_196sum.csv', index_col=0)
data = list(hc['sum_196'])

asd1 = pd.read_csv(
    '/Users/qingchen/Documents/code/NormativeModel/NM_Results/Result_GrayVol_GPR_10K_HCMDD/Step_5th_Subtype/step7_Subtype1_Positive_GreaterThan_196sum.csv', index_col=0)
data1 = list(asd1['sum_196'])

asd = pd.read_csv(
    '/Users/qingchen/Documents/code/NormativeModel/NM_Results/Result_GrayVol_GPR_10K_HCMDD/Step_5th_Subtype/step7_Subtype2_Positive_GreaterThan_196sum.csv', index_col=0)
data2 = list(asd['sum_196'])


# 创建DataFrame
df = pd.DataFrame({
    'Group': ['HCs'] * len(data) + ['Subtype1'] * len(data1) + ['Subtype2'] * len(data2) ,
    'Values': data + data1 + data2
})

# 绘制小提琴图
fig, ax = plt.subplots()
palette = {'HCs': '#8BACD1', 'Subtype1': '#C17F9E', 'Subtype2': '#FF7F50'}  # 修改颜色以区分
sns.violinplot(x='Group', y='Values', data=df, ax=ax, palette=palette)

# 设置y轴标签和其他图形属性
ax.set_ylabel('Sum of Positiv Deviation')  # 确保只设置一个ylabel
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks(range(len(df['Group'].unique())))
ax.set_xticklabels(df['Group'].unique())

# 两两t检验并添加注释
alpha = 0.05
group_names = df['Group'].unique()
group_indices = {name: idx for idx, name in enumerate(group_names)}

y_max = df['Values'].max()  # 获取整个数据集的最大值
plt.ylim(0, y_max)
for i in range(len(group_names)):
    for j in range(i + 1, len(group_names)):
        group1 = group_names[i]
        group2 = group_names[j]
        group1_data = df[df['Group'] == group1]['Values']
        group2_data = df[df['Group'] == group2]['Values']

        t_stat, p_value = ttest_ind(group1_data, group2_data)
        print(f'P value between {group1} and {group2} - ', p_value)

        if p_value < alpha:
            # 计算注释位置
            x_pos = (group_indices[group1] + group_indices[group2] + 1) / 2  # 加1以居中在两组之间
            #ax.text(x_pos, y_max + 2.2, '*', fontsize=12, ha='center', va='bottom', color='black')

        # 保存并显示图表
plt.savefig('./step6_2_SumOfPositiveDeviation.png', dpi=300)
plt.show()
