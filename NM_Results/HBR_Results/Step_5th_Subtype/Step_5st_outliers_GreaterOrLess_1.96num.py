import pandas as pd
'''
     被试水平，统计异常脑区的个数
'''
alldata = pd.read_csv('./step2_group_subtype1.csv',index_col=0)
#data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_Gradient_10K_HCMDD/staResults/Gradient_Z_AllHCestimate.csv')
sunID = alldata['subID']

data = alldata.iloc[:,1:]
print(data)
# 初始化异常值计数器 - 脑区水平
#outliers_per_subject = data.apply(
 #   lambda col: ((col <-1.96)).sum(), axis=0
#)

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
data.to_csv('./step5_subtype1_GreaterOrLess_RegionNum_1.96num.csv')

