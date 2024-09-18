import pandas as pd

# Load the data from the provided CSV files
hc_abnormal_region_df = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstrucIII/combat/HcOutAge.csv')
all_hc_grayvol_df = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstrucIII/combat/allHC_GrayVol_combat_final.csv')

# Display the first few rows of each dataframe to understand their structure

# Extract the list of subIDs to be removed
subIDs_to_remove = hc_abnormal_region_df['subID'].tolist()

# Filter the allHC_GrayVol_combat_final dataframe by removing the matching subIDs
filtered_all_hc_grayvol_df = all_hc_grayvol_df[~all_hc_grayvol_df['subID'].isin(subIDs_to_remove)]

# Save the filtered dataframe to a new CSV file
output_file_path = './allHC_GrayVol_combat_final.csv'
filtered_all_hc_grayvol_df.to_csv(output_file_path, index=False)


