import pandas as pd

# 读取数据
# data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/GrayVol246_Z_AllHCestimate.csv')
data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/GrayVol246_Z_AllMDD.csv')
print(data)

# 提取 subID 列
subID = data['subID']

# 去掉 subID 列，只保留数据列
data = data.iloc[:, 1:]

# 统计小于 -1.96 的脑区个数
outliers_negative = data.apply(lambda col: (col < -1.96).sum(), axis=0)

# 统计大于 1.96 的脑区个数
outliers_positive = data.apply(lambda col: (col > 1.96).sum(), axis=0)

# 合并正负异常值统计结果
outliers_total = outliers_negative + outliers_positive

print(outliers_total)

# 将 subID 列重新插入到数据中
data.insert(0, 'subID', subID)

# 将异常值统计结果添加到数据的最后一行
data.loc['outliers_counts'] = outliers_total

# 保存结果到 CSV 文件
# data.to_csv('./Step3_Z_AllHCestimate_NegativeBrainRegionNum.csv')
data.to_csv('./Step3_Z_AllMDD_NegativeBrainRegionNum.csv')