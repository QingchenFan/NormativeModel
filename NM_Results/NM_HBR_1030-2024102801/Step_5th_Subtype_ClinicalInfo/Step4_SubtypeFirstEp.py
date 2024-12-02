import pandas as pd
df = pd.read_csv("/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1030/StaResults/ClinicalInfo/allData_FirstEpisode.csv")
df1 = pd.read_csv("/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1030-2024102801/Step_5th_Subtype/"
                  "step2_group_subtype2.csv")

df_new = pd.merge(df, df1, on='subID', how='inner')


df_new.to_csv("./Subtype2_FirstEp.csv", index=False)