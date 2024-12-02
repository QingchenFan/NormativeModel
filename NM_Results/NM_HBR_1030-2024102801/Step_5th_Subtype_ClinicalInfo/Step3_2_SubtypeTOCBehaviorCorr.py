import numpy as np
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import statsmodels.stats.multitest as smm
import glob
import pandas as pd
# 第一步 构建数据 TOC和行为拼接到 csv

# csvdata = glob.glob("/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/ClinicalInfo/*.csv")
#
# for b in csvdata:
#   box = []
#   name = b.split('/')[-1].split('_')[-1][:-4]
#   print(name)
#   for i in range(1, 3):
#       file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/' \
#                   'subtype' + str(i) + '_TOC.csv'
#       # file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/' \
#       #          'subtype' + str(i) + '_DL_TOC.csv'
#       df1 = pd.read_csv(file_1)
#       df2 = pd.read_csv(b)
#       df_new = pd.merge(df2, df1, on='subID', how='inner')
#
#       box.append(df_new)
#       df_new.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/TOC/subtype'+str(i)+'_TOC_'+name+'.csv', index=False)
# print("Done")

# # 第二步计算相关

file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/TOC/*.csv'
csv = glob.glob(file_1)
for i in csv:

    sbty = i.split('/')[-1].split('_')
    beh = sbty[-1][:-3]
    stype = sbty[0]
    # Read the CSV files into DataFrames
    df1 = pd.read_csv(i)

    behscore = np.array(df1.iloc[:,1])

    x = np.array(df1.iloc[:,2])
    if x.size == 0:
        continue
    y = behscore

    corr, p_value = pearsonr(x, y)
    # if p_value < 0.05:
    #     print(stype,'-',beh, ' pearson correlation:', corr, 'p-value:', p_value)

    scorr, sp_value = spearmanr(x, y)
    #print(stype, '-', beh, ' spearman correlation:', scorr, 'p-value:', sp_value)
    if sp_value < 0.05:
        print(stype,'-',beh, ' spearman correlation:', scorr, 'p-value:', sp_value)




