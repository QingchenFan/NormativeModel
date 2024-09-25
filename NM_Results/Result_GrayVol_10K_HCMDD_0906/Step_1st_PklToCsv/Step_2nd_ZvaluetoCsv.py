import pandas as pd

Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0906/NMResults/Z_AllHCestimate.pkl')
#Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0906/NMResults/Z_AllHCMDD.pkl')
label = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstrucIII/combat/allHC_GrayVol_combat_final_0906.csv')

brainRegion = label.columns.tolist()
del brainRegion[0:5]


Z_AllHCestimate.columns = brainRegion

subIDs = label['subID']

zvalue = pd.concat([subIDs, Z_AllHCestimate], axis=1)

zvalue.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0906/StaResults/GrayVol_Z_AllHCestimate.csv')