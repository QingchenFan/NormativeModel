import pandas as pd
'''
    被试水平，统计异常脑区的大于1.96 之和
'''
# 读取CSV文件，假设没有列标题，因此header=None
data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/Longitudinal/GrayVol246_Z_mdd52.csv')

sunID = data['subID']
data = data.iloc[:, 1:]
# 打印原始数据
print(data)

# 对每一行应用函数，计算大于1.96的值的总和
outliers_per_subject = data.apply(
    lambda row: row[row > 1.96].sum(), axis=1
)

# outliers_per_subject = data.apply(
#     lambda col: col[(col >1.96) | (col <-1.96)].sum(), axis=0
# )

# 打印异常值总和
print(outliers_per_subject)

# 将计算结果作为新列添加到数据框中
data['sum_196'] = outliers_per_subject
data.insert(0, 'subID', sunID)
# 将更新后的数据框写入新的CSV文件
data.to_csv('./MDD52_Positive_GreaterThan_196sum.csv', index=False)