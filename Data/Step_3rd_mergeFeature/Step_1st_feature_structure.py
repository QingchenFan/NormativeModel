import glob
import pandas as pd

# --------HCP features ----------
label = pd.read_csv('/Volumes/QCI/HCPData/HCP1200_age_gender.csv')
hcpGrayVol = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/HCPGrayVol.csv')
hcpGrayVol_df = pd.merge(label, hcpGrayVol, on='subID', how='inner')
hcpGrayVol_df.to_csv('./HCPGrayVol.csv',index=False)

HCPSurfArea = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/HCPSurfArea.csv')
HCPSurfArea_df = pd.merge(label, HCPSurfArea, on='subID', how='inner')
HCPSurfArea_df.to_csv('./HCPSurfArea.csv',index=False)

HCPThickAvg = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/HCPThickAvg.csv')
HCPThickAvg_df = pd.merge(label, HCPThickAvg, on='subID', how='inner')
HCPThickAvg_df.to_csv('./HCPThickAvg.csv',index=False)



