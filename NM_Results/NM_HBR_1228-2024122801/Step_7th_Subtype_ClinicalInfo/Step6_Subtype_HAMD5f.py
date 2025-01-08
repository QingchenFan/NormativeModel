# import scipy.stats as stats
# import pandas as pd
# import numpy as np
# def cohen_d(group1, group2):
#     """
#     计算Cohen's d
#     :param group1: 第一组数据（一维数组或列表）
#     :param group2: 第二组数据（一维数组或列表）
#     :return: Cohen's d值
#     """
#     n1, n2 = len(group1), len(group2)
#     mean1, mean2 = np.mean(group1), np.mean(group2)
#     var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
#     pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
#     return (mean1 - mean2) / pooled_std
#
#
# subtype1_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/subtype1_ZvalueHAMD_5f.csv'
# subtype2_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/subtype2_ZvalueHAMD_5f.csv'
# subtype1_data = pd.read_csv(subtype1_path)
# subtype2_data = pd.read_csv(subtype2_path)
# subtype1_mark = subtype1_data['f5']
# subtype2_mark = subtype2_data['f5']
# t_stat, p_value = stats.ttest_ind(subtype1_mark, subtype2_mark)
# cod = cohen_d(subtype1_mark, subtype2_mark)
# print(cod)
# print(' t_stat: ',t_stat,' p_value: ', p_value)
#
# import seaborn as sns
# import matplotlib.pyplot as plt
# # 准备用于绘制小提琴图的数据，将两个亚型的数据合并到一个DataFrame中，并添加一列用于区分亚型
# data_for_plot = pd.DataFrame({
#     'Value': pd.concat([subtype1_mark, subtype2_mark]),
#     'Subtype': ['Subtype1'] * len(subtype1_mark) + ['Subtype2'] * len(subtype2_mark)
# })
# fig, ax = plt.subplots(figsize=(10, 6))
# palette = {'HCs': '#8BACD1', 'Subtype1': '#C17F9E', 'Subtype2': '#80B1D3'}
# # 绘制小提琴图
# sns.violinplot(x='Subtype', y='Value', data=data_for_plot, palette=palette)
# ax.set_yticks([0, 2, 4, 6, 8])
# ax.tick_params(axis='y', labelsize=12)
# ax.tick_params(axis='x', labelsize=12)
# # 去掉上面和右边的线条
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
#
# # 自定义x轴和y轴的线条粗细
# ax.spines['bottom'].set_linewidth(1.0)
# ax.spines['left'].set_linewidth(1.0)
# # 设置图形标题、坐标轴标签等
# #plt.title("Distribution Comparison of Subtype1 and Subtype2")
# plt.xlabel("Subtype", size=14)
# plt.ylabel("Sleep Score", size=14)
#
# # 展示图形
# plt.show()
import scipy.stats as stats
import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import statsmodels.stats.multitest as smm
import seaborn as sns
import matplotlib.pyplot as plt


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


subtype1_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/subtype1_ZvalueHAMD_5f.csv'
subtype2_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/subtype2_ZvalueHAMD_5f.csv'
subtype1_data = pd.read_csv(subtype1_path)
subtype2_data = pd.read_csv(subtype2_path)
a = ['f1', 'f2', 'f3', 'f4', 'f5']
pbox = []
for i in a:
    subtype1_mark = subtype1_data[i]
    subtype2_mark = subtype2_data[i]

    t_stat, p_value = stats.ttest_ind(subtype1_mark, subtype2_mark)
    pbox.append(p_value)
    cod = cohen_d(subtype1_mark, subtype2_mark)

    print(cod)
    print(i, ' t_stat: ', t_stat, ' p_value: ', p_value)
rejected, fdr_pvalue, _, _ = smm.multipletests(pbox, method='fdr_bh')

print(fdr_pvalue)
# # 准备用于绘制箱体图的数据，将两个亚型的数据合并到一个DataFrame中，并添加一列用于区分亚型
# data_for_plot = pd.DataFrame({
#     'Value': pd.concat([subtype1_mark, subtype2_mark]),
#     'Subtype': ['Subtype1'] * len(subtype1_mark) + ['Subtype2'] * len(subtype2_mark)
# })
#
# fig, ax = plt.subplots(figsize=(10, 6))
# palette = {'HCs': '#8BACD1', 'Subtype1': '#C17F9E', 'Subtype2': '#80B1D3'}
#
# # 绘制箱体图
# box_plot = sns.boxplot(x='Subtype', y='Value', data=data_for_plot, palette=palette, width=0.3)
#
# # 获取箱线图的各个组成部分，以便设置线条宽度
# lines = box_plot.lines
# for line in lines:
#     line.set_linewidth(1.5)  # 将线宽设置为2.0，可根据实际需求调整该值
#
# ax.set_yticks([0, 2, 4, 6, 8])
# ax.tick_params(axis='y', labelsize=12)
# ax.tick_params(axis='x', labelsize=12)
#
# # 去掉上面和右边的线条
# ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
#
# # 自定义x轴和y轴的线条粗细
# ax.spines['bottom'].set_linewidth(1.0)
# ax.spines['left'].set_linewidth(1.0)
#
# # 设置图形标题、坐标轴标签等
# # plt.title("Distribution Comparison of Subtype1 and Subtype2")
# plt.xlabel("Subtype", size=14)
# plt.ylabel("Sleep Score", size=14)
#
# # 展示图形
# plt.show()