import glob
import pandas as pd
from scipy.io import savemat,loadmat

#--------HCP features ----------
HCP_datapath = '/Volumes/QCI/HCPData/HCP_IndividualGradient/*'
HCPdata = glob.glob(HCP_datapath)

label = pd.read_csv('/Volumes/QCI/HCPData/HCP1200_age_gender.csv')
nhcp = pd.DataFrame()
for i in HCPdata:
    subId = i.split('/')[5][0:10]
    print('---->',subId)
    hcpdata = loadmat(i)['data'][:,0:1].T
    hcpdata = pd.DataFrame(hcpdata)
    item = label.loc[label['participant_id'] == subId]

    result = pd.concat([item.reset_index(drop=True), hcpdata], axis=1)
    print(result)
    nhcp = pd.concat([nhcp,result])

nhcp.to_csv('./hcpfeature.csv', index=False)

