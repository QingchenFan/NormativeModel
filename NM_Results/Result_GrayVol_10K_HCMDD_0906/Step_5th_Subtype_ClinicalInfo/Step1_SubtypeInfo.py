import pandas as pd

# 读取两个CSV文件
file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/step2_group_subtype1.csv'
file_2 = '/Volumes/QCI/NormativeModel/Prediction/Data/sum_BrainPro_ClinicalInfo.csv'


# Read the CSV files into DataFrames
df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)


# Filter rows from df2 where 'subID' matches with df1
filtered_df = df2[df2['subID'].isin(df1['subID'])]
# BrainPro
df2['subID'] = df2['subID'].astype(str)

filtered_df = df2[df2['subID'].isin(df1['subID'])]

# Save the filtered dataframe to a new CSV file
output_file = "./subtype1_BrainPro_Clinicalinfo.csv"
filtered_df.to_csv(output_file, index=False)