
import pandas as pd
# 已知表格从另一个表格中获取
# 读取两个CSV文件
file_1 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/GrayVol_Z_AllHCMDD_BrainPro_PD.csv'
file_2 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/step2_group_subtype2_tmp.csv'


# Read the CSV files into DataFrames
df1 = pd.read_csv(file_1)
df2 = pd.read_csv(file_2)

# Extract the 'subID' column from both DataFrames
common_subIDs = df1['subID'].isin(df2['subID'])

# Filter rows from df2 where 'subID' matches with df1
filtered_df = df2[df2['subID'].isin(df1['subID'])]



# Save the filtered dataframe to a new CSV file
output_file = "./BrainPro_PD2_s1s2.csv"
filtered_df.to_csv(output_file, index=False)