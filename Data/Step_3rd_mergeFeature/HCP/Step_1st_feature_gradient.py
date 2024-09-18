import glob
import pandas as pd
from scipy.io import savemat,loadmat
# --------HCP features ----------
# HCP_datapath = '/Volumes/QCI/HCPData/HCP_IndividualGradient/*'
# HCPdata = glob.glob(HCP_datapath)
#
# label = pd.read_csv('/Volumes/QCI/HCPData/HCP1200_age_gender.csv')
# nhcp = pd.DataFrame()
# for i in HCPdata:
#     subId = i.split('/')[5][0:10]
#     print('---->',subId)
#     hcpdata = loadmat(i)['data'][:,0:1].T
#     hcpdata = pd.DataFrame(hcpdata)
#     item = label.loc[label['participant_id'] == subId]
#
#     result = pd.concat([item.reset_index(drop=True), hcpdata], axis=1)
#     print(result)
#     nhcp = pd.concat([nhcp,result])

#nhcp.to_csv('./hcpfeature.csv', index=False)

# # --------Data135 HC features --------
# HClabel = pd.read_csv('/Volumes/QCI/NormativeModel/Data135/HClabel.csv')
# HCdata = glob.glob('/Volumes/QCI/NormativeModel/Data135/HC/Data135_IndividualGradient/*')
# nhc = pd.DataFrame()
# for j in HCdata:
#     hcsubId = j.split('/')[7][4:9]
#     print('---->',hcsubId)
#     hcdata = loadmat(j)['data'][:, 0:1].T
#     hcdata = pd.DataFrame(hcdata)
#
#     nhcitem = HClabel.loc[HClabel['participant_id'] == hcsubId]
#     print(nhcitem)
#     nhcresult = pd.concat([nhcitem.reset_index(drop=True), hcdata], axis=1)
#     nhc = pd.concat([nhc, nhcresult])
# nhc.to_csv('./hcfeature.csv', index=False)

# -------- Data135 MDD features --------
MDDlabel = pd.read_csv('/Volumes/QCI/NormativeModel/Data135/MDDlabel.csv')
MDDdata = glob.glob('/Volumes/QCI/NormativeModel/Data135/MDD/Data135_IndividualGradient/*')
nmdd = pd.DataFrame()
for p in MDDdata:
    mddsubId = p.split('/')[7][4:10]
    print('---->',mddsubId)
    mdddata = loadmat(p)['data'][:, 0:1].T
    mdddata = pd.DataFrame(mdddata)

    mdditem = MDDlabel.loc[MDDlabel['participant_id'] == mddsubId]
    print(mdditem)
    mddresult = pd.concat([mdditem.reset_index(drop=True), mdddata], axis=1)
    nmdd = pd.concat([nmdd, mddresult])
nmdd.to_csv('./mddfeature.csv', index=False)