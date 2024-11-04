
import pandas as pd

# 读取两个CSV文件
file_2 = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/GrayVol_Z_AllHCMDD_brainPro.csv'
file_1 = '/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/BrainPro/BrainProPDMDDGrayVol_sum.csv'





brainpro_df = pd.read_csv(file_1)
grayvol_df = pd.read_csv(file_2)

# Extract the 'subID' column from the first file
sub_ids = brainpro_df['subID']

# Filter rows in the second file where 'subID' matches
filtered_df = grayvol_df[grayvol_df['subID'].isin(sub_ids)]

# Save the filtered dataframe to a new CSV file
output_file = "./GrayVol_Z_AllHCMDD_BrainPro_PD.csv"
filtered_df.to_csv(output_file, index=False)