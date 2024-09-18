import glob
import pandas as pd

# --------HCP features ----------
label = pd.read_csv('/Volumes/QCI/HCPData/HCP1200_age_gender.csv')
hcpGrayVol = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/HCP/HCPGrayVol.csv')
hcpGrayVol_df = pd.merge(label, hcpGrayVol, on='subID', how='inner')
hcpGrayVol_df.to_csv('./HCPGrayVol_sum.csv',index=False)
#
# HCPSurfArea = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/HCPSurfArea.csv')
# HCPSurfArea_df = pd.merge(label, HCPSurfArea, on='subID', how='inner')
# HCPSurfArea_df.to_csv('./HCPSurfArea.csv',index=False)
#
# HCPThickAvg = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/HCPThickAvg.csv')
# HCPThickAvg_df = pd.merge(label, HCPThickAvg, on='subID', how='inner')
# HCPThickAvg_df.to_csv('./HCPThickAvg.csv',index=False)
#


# # --------Data135 HC features --------
# Data135HClabel = pd.read_csv('/Volumes/QCI/NormativeModel/Data135/HClabel.csv')
# Data135HCGrayVol = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCP_DATA135_Structure/Data135HCGrayVol.csv')
# Data135HCGrayVol_df = pd.merge(Data135HClabel, Data135HCGrayVol, on='subID', how='inner')
# Data135HCGrayVol_df.to_csv('./Data135HCGrayVol.csv', index=False)
#
#
# Data135HCSurfArea = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCP_DATA135_Structure/Data135HCSurfArea.csv')
# Data135HCSurfArea_df = pd.merge(Data135HClabel, Data135HCSurfArea, on='subID', how='inner')
# Data135HCSurfArea_df.to_csv('./Data135HCSurfArea.csv', index=False)
#
# Data135HCThickAvg = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCP_DATA135_Structure/Data135HCThickAvg.csv')
# Data135HCThickAvg_df = pd.merge(Data135HClabel, Data135HCThickAvg, on='subID', how='inner')
# Data135HCThickAvg_df.to_csv('./Data135HCThickAvg.csv', index=False)

## -------- Data135 MDD features --------
# Data135MDDlabel = pd.read_csv('/Volumes/QCI/NormativeModel/Data135/MDDlabel.csv')
# Data135MDDGrayVol = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCP_DATA135_Structure/Data135MDDGrayVol.csv')
# Data135MDDGrayVol_df = pd.merge(Data135MDDlabel, Data135MDDGrayVol, on='subID', how='inner')
# Data135MDDGrayVol_df.to_csv('./Data135MDDGrayVol.csv', index=False)
#
# Data135MDDSurfArea = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCP_DATA135_Structure/Data135MDDSurfArea.csv')
# Data135MDDSurfArea_df = pd.merge(Data135MDDlabel, Data135MDDSurfArea, on='subID', how='inner')
# Data135MDDSurfArea_df.to_csv('./Data135MDDSurfArea.csv', index=False)
#
# Data135MDDThickAvg = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/HCP_DATA135_Structure/Data135MDDThickAvg.csv')
# Data135MDDThickAvg_df = pd.merge(Data135MDDlabel, Data135MDDThickAvg, on='subID', how='inner')
# Data135MDDThickAvg_df.to_csv('./Data135MDDThickAvg.csv', index=False)
