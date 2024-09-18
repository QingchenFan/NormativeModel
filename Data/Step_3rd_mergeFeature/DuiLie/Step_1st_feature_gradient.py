import glob
import pandas as pd
from scipy.io import savemat,loadmat


# # --------HC features --------
HClabel = pd.read_csv('/Volumes/QCI/NormativeModel/DuiLie/DLHClabel.csv')
HCdata = glob.glob('/Volumes/QCI/NormativeModel/DuiLie/HC/DuiLie_IndividualGradient/*')
nhc = pd.DataFrame()
for j in HCdata:
    hcsubId = j.split('/')[7][4:12]
    print('---->',hcsubId)

    hcdata = loadmat(j)['data'][:, 0:1].T
    hcdata = pd.DataFrame(hcdata)

    nhcitem = HClabel.loc[HClabel['subID'] == hcsubId]
    print(nhcitem)
    nhcresult = pd.concat([nhcitem.reset_index(drop=True), hcdata], axis=1)
    nhc = pd.concat([nhc, nhcresult])
nhc.to_csv('./DLHC_Gradientfeature.csv', index=False)

# -------- MDD features --------
# MDDlabel = pd.read_csv('/Volumes/QCI/NormativeModel/Data135/MDDlabel.csv')
# MDDdata = glob.glob('/Volumes/QCI/NormativeModel/Data135/MDD/Data135_IndividualGradient/*')
# nmdd = pd.DataFrame()
# for p in MDDdata:
#     mddsubId = p.split('/')[7][4:10]
#     print('---->',mddsubId)
#     mdddata = loadmat(p)['data'][:, 0:1].T
#     mdddata = pd.DataFrame(mdddata)
#
#     mdditem = MDDlabel.loc[MDDlabel['participant_id'] == mddsubId]
#     print(mdditem)
#     mddresult = pd.concat([mdditem.reset_index(drop=True), mdddata], axis=1)
#     nmdd = pd.concat([nmdd, mddresult])
# nmdd.to_csv('./mddfeature.csv', index=False)