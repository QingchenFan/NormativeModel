import pandas as pd

Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1028/NMResults/Z_mdd.pkl')
label = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1028/NMResults/allMDDGrayVol246_sum.csv')
#Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1028/NMResults/Z_estimate.pkl')
#label = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1028/NMResults/allHC_te.csv')

brainRegion = label.columns.tolist()
del brainRegion[0:7]


Z_AllHCestimate.columns = brainRegion

subIDs = label['subID']

zvalue = pd.concat([subIDs, Z_AllHCestimate], axis=1)

zvalue.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1028/StaResults/GrayVol246_Z_AllMDD.csv')