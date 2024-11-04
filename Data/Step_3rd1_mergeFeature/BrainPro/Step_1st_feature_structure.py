import glob
import pandas as pd

# # --------BrainPro HC features --------
BrainProHClabel = pd.read_csv('/Volumes/QCI/NormativeModel/BrainProject/HClabel.csv')
BrainProHCGrayVol = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/StructureFeature_246/BrainPro/BrainProHCGrayVol_246.csv')
BrainProHCGrayVol_df = pd.merge(BrainProHClabel, BrainProHCGrayVol, on='subID', how='inner')
BrainProHCGrayVol_df.to_csv('./BrainProHCGrayVol246_sum.csv', index=False)
#

## -------- BrainPro MDD features --------
BrainProMDDlabel = pd.read_csv('/Volumes/QCI/NormativeModel/BrainProject/NPlabel.csv')
BrainProMDDGrayVol = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/StructureFeature_246/BrainPro/BrainProNPGrayVol_246.csv')
BrainProMDDGrayVol_df = pd.merge(BrainProMDDlabel, BrainProMDDGrayVol, on='subID', how='inner')
BrainProMDDGrayVol_df.to_csv('./BrainProNPMDDGrayVol246_sum.csv', index=False)


BrainProPDMDDlabel = pd.read_csv('/Volumes/QCI/NormativeModel/BrainProject/PDlabel.csv')
BrainProPDMDDGrayVol = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/StructureFeature_246/BrainPro/BrainProPDGrayVol_246.csv')
BrainProPDMDDGrayVol_df = pd.merge(BrainProPDMDDlabel, BrainProPDMDDGrayVol, on='subID', how='inner')
BrainProPDMDDGrayVol_df.to_csv('./BrainProPDMDDGrayVol246_sum.csv', index=False)
