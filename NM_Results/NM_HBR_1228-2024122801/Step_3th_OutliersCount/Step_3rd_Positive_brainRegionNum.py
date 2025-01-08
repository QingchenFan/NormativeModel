import pandas as pd
'''
     脑区水平，统计异常脑区的个数
     脑区水平就是看这个脑区上有多少被试是正的，多少是负的。被试水平就是，一个被试，400个脑区都看，看哪些是正，哪些是负
     HC MDD 执行两次代码
'''
data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/GrayVol246_Z_AllHCestimate.csv')
#data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/GrayVol246_Z_AllMDD.csv')

print(data)
sunID = data['subID']

data = data.iloc[:, 1:]
# 初始化异常值计数器 - 脑区水平
outliers_brainRegion_subject = data.apply(
   lambda col: ((col > 1.96)).sum(), axis=0
)

print(outliers_brainRegion_subject)
data.insert(0, 'subID', sunID)
data.loc['outliers_counts']=outliers_brainRegion_subject

data.to_csv('./Step3_Z_AllHCestimate_PositiveBrainRegionNum.csv')
#data.to_csv('./Step3_Z_AllMDD_PositiveBrainRegionNum.csv')