import pandas as pd
# 需要对 step2_group_subtype1 step2_group_subtype2 subID进行处理
# 读取两个CSV文件
file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/GrayVol246_Z_AllMDD.csv'
file_2 = '/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1129-2024112901/Step_7th_Subtype_ClinicalInfo/subtype2_ZvalueHAMD_temp.csv'



# Read the CSV files into DataFrames
df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)

df_new = pd.merge(df2, df1, on='subID', how='inner')

df_new.to_csv('./subtype2_ZvalueHAMD.csv',index=False)
