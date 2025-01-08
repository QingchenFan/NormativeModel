import pandas as pd
 # step2 可以删除 大于3个标准差 脑区个数 的被试。
# Load the data from the provided CSV files

hc_abnormal_region_df = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1216/Feature/HC_abnormalregion_3.csv')
all_hc_grayvol_df = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1216/Feature/AllHC_GrayVol_all246_II.csv')


# Display the first few rows of each dataframe to understand their structure

# Extract the list of subIDs to be removed
subIDs_to_remove = hc_abnormal_region_df['subID'].tolist()

# Filter the allHC_GrayVol_combat_final dataframe by removing the matching subIDs
filtered_all_hc_grayvol_df = all_hc_grayvol_df[~all_hc_grayvol_df['subID'].isin(subIDs_to_remove)]

# Save the filtered dataframe to a new CSV file
output_file_path = './AllHC_GrayVol_all246_III.csv'
filtered_all_hc_grayvol_df.to_csv(output_file_path, index=False)


