import pandas as pd
# 需要对 step2_group_subtype1 step2_group_subtype2 subID进行处理
# 读取两个CSV文件
file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1128/StaResults/' \
         'GrayVol246_Z_AllMDD.csv'
file_2 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1128/StaResults/' \
         'allData_FirstEpisode.csv'



# Read the CSV files into DataFrames
df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)

df_new = pd.merge(df2, df1, on='subID', how='inner')

df_new.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1128/StaResults'
              '/allMDD_FirstEpisode.csv',index=False)
