import pandas as pd

Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_5K_HCMDD_1022/NMResults/Z_AllHCestimate.pkl')
#Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_5K_HCMDD_1022/NMResults/Z_AllMDD.pkl')
label = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_5K_HCMDD_1022/NMResults/allHC_GrayVol246_combat_final.csv')

brainRegion = label.columns.tolist()
del brainRegion[0:7]


Z_AllHCestimate.columns = brainRegion

subIDs = label['subID']

zvalue = pd.concat([subIDs, Z_AllHCestimate], axis=1)

zvalue.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_5K_HCMDD_1022/StaResults/GrayVol246_Z_AllHCestimate.csv')