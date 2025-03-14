import pandas as pd
'''
     被试水平，统计异常脑区的个数
'''
data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_5K_HCMDD_1022/StaResults/'
                   'GrayVol246_Z_AllHCestimate.csv')
data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_5K_HCMDD_1022/StaResults/'
                   'GrayVol246_Z_AllMDD.csv')
data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10k_HCMDD_0906/StaResults/GrayVol_Z_AllHCMDD.csv')
sunID = data['subID']

data = data.iloc[:,1:]
print(data)
# 初始化异常值计数器 - 脑区水平
outliers_brainRegion_subject = data.apply(
   lambda col: ((col <-1.96)).sum(), axis=0
)

#统计每个被式异常数
outliers_per_subject = data.apply(
     lambda row: ((row > 1.96) | (row <-1.96)).sum(), axis=1
)

outliers_num_subject196 = data.apply(
     lambda row: ((row > 1.96)).sum(), axis=1
)

outliers_num_subject_196 = data.apply(
     lambda row: ((row < -1.96)).sum(), axis=1
)
data['outliers_num1.96'] = outliers_num_subject196
data['outliers_num-1.96'] = outliers_num_subject_196
data['outliers_counts']=outliers_per_subject

data.insert(0, 'sunID', sunID)
#data.to_csv('./Step1_Z_AllHCestimate_GreaterOrLess_1.96num.csv')
data.to_csv('./GPR_0906_Step1_Z_AllMDD_GreaterOrLess_1.96num.csv')


