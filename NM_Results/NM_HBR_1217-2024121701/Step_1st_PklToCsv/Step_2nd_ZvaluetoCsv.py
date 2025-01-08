import pandas as pd

from scipy.io import savemat
# TODO: HC MDD 执行两次
# Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1216/NMResults/Z_mdd.pkl')
# label = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1216/Feature/AllMDD_GrayVol_all246_III.csv')

Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1216/NMResults/Z_estimate.pkl')
label = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1216/NMResults/allHC_te.csv')


brainRegion = label.columns.tolist()
del brainRegion[0:5]
print(brainRegion)


Z_AllHCestimate.columns = brainRegion

subIDs = label['subID']

zvalue = pd.concat([subIDs, Z_AllHCestimate], axis=1)

# zvalue.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1216/StaResults'
#               '/GrayVol246_Z_AllMDD.csv')

zvalue.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1216/StaResults'
              '/GrayVol246_Z_AllHCestimate.csv')