import pandas as pd
import matplotlib.pyplot as plt
'''
    被试水平，统计异常脑区个数的 人数 例如有一个脑区异常的人数 二个脑区异常的人数
'''
# 假设的CSV文件名和分组列名
csv_file = '/Users/qingchen/Documents/code/NormativeModel/NM_Results/Result_GrayVol_GPR_10K_HCMDD/Step_3th_OutliersCount/Step1_Z_AllMDD_GreaterOrLess_1.96num.csv'
group_column = 'outliers_counts'

# 读取CSV文件
df = pd.read_csv(csv_file)

num = len(df['sunID'])

# 假设数据集中有一个名为Group的列，包含分组信息
# 统计每组中'out'列大于等于1、3、5的个数
group1_ge1 = df[(df['outliers_num1.96'] >= 1)]['outliers_num1.96'].count()/num
group1_ge3 = df[(df['outliers_num1.96'] >= 3)]['outliers_num1.96'].count()/num
group1_ge5 = df[(df['outliers_num1.96'] >= 5)]['outliers_num1.96'].count()/num
group1_ge7 = df[(df['outliers_num1.96'] >= 7)]['outliers_num1.96'].count()/num
group1_ge9 = df[(df['outliers_num1.96'] >= 9)]['outliers_num1.96'].count()/num
group1_ge11 = df[(df['outliers_num1.96'] >= 11)]['outliers_num1.96'].count()/num

group2_ge1 = df[(df['outliers_num-1.96'] >= 1)]['outliers_num-1.96'].count()/num
group2_ge3 = df[(df['outliers_num-1.96'] >= 3)]['outliers_num-1.96'].count()/num
group2_ge5 = df[(df['outliers_num-1.96'] >= 5)]['outliers_num-1.96'].count()/num
group2_ge7 = df[ (df['outliers_num-1.96'] >= 7)]['outliers_num-1.96'].count()/num
group2_ge9 = df[(df['outliers_num-1.96'] >= 9)]['outliers_num-1.96'].count()/num
group2_ge11 = df[(df['outliers_num-1.96'] >= 11)]['outliers_num-1.96'].count()/num

# group1_ge1 = df[(df['outliers_num1.96'] >= 1)]['outliers_num1.96'].count()
# group1_ge3 = df[ (df['outliers_num1.96'] >= 3)]['outliers_num1.96'].count()
# group1_ge5 = df[ (df['outliers_num1.96'] >= 5)]['outliers_num1.96'].count()
# group1_ge7 = df[(df['outliers_num1.96'] >= 7)]['outliers_num1.96'].count()
# group1_ge9 = df[(df['outliers_num1.96'] >= 9)]['outliers_num1.96'].count()
# group1_ge11 = df[(df['outliers_num1.96'] >= 11)]['outliers_num1.96'].count()
#
# group2_ge1 = df[(df['outliers_num-1.96'] >= 1)]['outliers_num-1.96'].count()
# group2_ge3 = df[(df['outliers_num-1.96'] >= 3)]['outliers_num-1.96'].count()
# group2_ge5 = df[(df['outliers_num-1.96'] >= 5)]['outliers_num-1.96'].count()
# group2_ge7 = df[ (df['outliers_num-1.96'] >= 7)]['outliers_num-1.96'].count()
# group2_ge9 = df[(df['outliers_num-1.96'] >= 9)]['outliers_num-1.96'].count()
# group2_ge11 = df[(df['outliers_num-1.96'] >= 11)]['outliers_num-1.96'].count()

# 将统计结果整理为列表
conditions = ['>=1', '>=3', '>=5','>=7', '>=9', '>=11']
group1_counts = [group1_ge1, group1_ge3, group1_ge5,group1_ge7, group1_ge9, group1_ge11]
group2_counts = [group2_ge1, group2_ge3, group2_ge5,group2_ge7, group2_ge9, group2_ge11]
print(group1_counts)
print(group2_counts)# 绘制柱状图
# 16进制颜色代码
color_group1 = '#62B197'  # Group 1的颜色
color_group2 = '#E18E6D'  # Group 2的颜色

plt.figure(figsize=(10, 6))  # 设置图形大小
# 定义x轴的位置
x_positions = range(len(conditions))
# 绘制第一组的柱状图
plt.bar([x + 0.3 for x in x_positions], group1_counts, width=0.4, color=color_group1, label='Positive')

# 绘制第二组的柱状图，错开显示
plt.bar([x - 0.2 for x in x_positions], group2_counts, width=0.4, color=color_group2, label='Negative')
# 设置图例
plt.legend()

ax = plt.gca()
# 去除上边框和右边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 去除刻度线 设置轴上数字大小
plt.gca().tick_params(axis='x', which='both', width=0, labelsize=12)
plt.gca().tick_params(axis='y', which='both', width=0, labelsize=12)

# 设置下边框和左边框的线宽
ax.spines['bottom'].set_linewidth(1)
ax.spines['left'].set_linewidth(1)

# 设置标题和轴标签
plt.title('The distribution of the number of regions per patient with extreme deviations')
plt.xlabel('Number of Extremely Deviated Regions')
plt.ylabel('Percentage of Subhects(%)')

# 显示x轴的标签
plt.xticks([i + 0.2 for i in range(len(conditions))], conditions)

# 显示图表
plt.tight_layout()  # 调整布局以适应标签
plt.savefig('./step3_NumberOfExtremelyDeviatedRegionsNum.png',dpi=300)

plt.show()