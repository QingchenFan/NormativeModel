import pandas as pd
import statsmodels.stats.multitest as smm
import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
# 感觉计算这个没太大意义！
# 需要对 step2_group_subtype1 step2_group_subtype2 subID进行处理
# 读取两个CSV文件
file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/' \
         'GrayVol246_Z_AllMDD.csv'
file_2 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/ClinicalInfo/' \
         'allDataMDD_HAMD.csv'



# Read the CSV files into DataFrames
df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)

df_new = pd.merge(df2, df1, on='subID', how='inner')

df_new.to_csv('./Step6_allDataMDD_Zvalue_HAMD.csv', index=False)



# Read the CSV files into DataFrames
df1 = pd.read_csv('./Step6_allDataMDD_Zvalue_HAMD.csv')

behscore = np.array(df1.iloc[:, 1])

brainRegion = df1.columns.tolist()
cl = brainRegion[1:2]

del brainRegion[:2]

srvalue = []
spvalue = []
rvalue = []
pvalue = []
regionbox = []
for i in brainRegion:
    regionbox.append(i)
    x = np.array(df1[i])

    y = behscore

    corr, p_value = pearsonr(x, y)
    rvalue.append(corr)
    pvalue.append(p_value)

    scorr, sp_value = spearmanr(x, y)
    srvalue.append(scorr)
    spvalue.append(sp_value)

    # print(f"Spearman相关系数: {scorr}", f"p值: {sp_value}")
    # print(f"Pearson相关系数: {corr}", f"p值: {p_value}")

# 对p值进行FDR校正
rejected, fdr_pvalue, _, _ = smm.multipletests(pvalue, method='fdr_bh')
srejected, sfdr_pvalue, _, _ = smm.multipletests(spvalue, method='fdr_bh')

# 创建DataFrame，将rvalue、pvalue、fdr_pvalue对应保存
result_df = pd.DataFrame({
    'region': regionbox,

    'rvalue-s': srvalue,
    'pvalue-s': spvalue,
    'fdr-pvalue-s': sfdr_pvalue,

    'rvalue': rvalue,
    'pvalue': pvalue,
    'fdr-pvalue': fdr_pvalue,

})

# 将结果保存到CSV文件中，可根据实际需求修改文件路径及文件名
result_df.to_csv('./Step6_allDataMDD_Zvalue_HAMDCorr.csv', index=False)