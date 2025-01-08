import pandas as pd

from scipy.io import savemat
# TODO: HC MDD 执行两次
Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/Z_wkkwwmdd.pkl')
label = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/Feature/allMDDGrayVol246_sum_1129.csv')

# Z_AllHCestimate = pd.read_pickle('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/Z_estimate.pkl')
# label = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/allHC_te.csv')


brainRegion = label.columns.tolist()
del brainRegion[0:7]

Z_AllHCestimate.columns = brainRegion

subIDs = label['subID']

zvalue = pd.concat([subIDs, Z_AllHCestimate], axis=1)

zvalue.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/Longitudinal/GrayVol246_Z_wkkwww.csv')

# zvalue.to_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults'
#               '/GrayVol246_Z_AllHCestimate.csv')