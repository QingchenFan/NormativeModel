import pandas as pd
df = pd.read_csv("/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/allData_FirstEpisode.csv")
df1 = pd.read_csv("/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1129-2024112901/Step_5th_Subtype/"
                  "step2_group_subtype1.csv")

df_new = pd.merge(df, df1, on='subID', how='inner')


df_new.to_csv("./Subtype1_FirstEp.csv", index=False)