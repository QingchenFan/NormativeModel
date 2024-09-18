
import pandas as pd

file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/GrayVol_Z_AllHCMDD_BrainPro_NP.csv'
file_2 = '/Volumes/QCI/NormativeModel/ClinicalInf/BrainPro_NP_info.csv'


# Read the CSV files into DataFrames
df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)

df_new = pd.merge(df2, df1, on='subID', how='inner')

df_new.to_csv('./BrainPro_NP_feature_prediction.csv',index=False)
