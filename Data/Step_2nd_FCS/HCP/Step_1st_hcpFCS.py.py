import glob

from numpy import arctanh
from scipy.io import savemat,loadmat
import numpy as np
import pandas as pd

def calculate_z_scores(data):
    mean = np.mean(data)
    std = np.std(data)
    z_scores = (data - mean) / std
    return z_scores

FCpath = glob.glob('/Volumes/QCI/HCPData/HCP_Schaefer400FC_mat/*')

label = pd.read_csv('/Volumes/QCI/HCPData/HCP1200_age_gender.csv')
nhcp = pd.DataFrame()
for i in FCpath:
    subId = i.split('/')[5][0:10]
    print('---->',subId)
    data = loadmat(i)['data']
    data = arctanh(data)
    data[np.isinf(data)] = 0
    data[data < 0.2] = 0

    res = np.sum(data, axis=0)
    print(res.shape)
    res = calculate_z_scores(res)
    print(res.T)
    print(res.shape)


    HCFvalue = pd.DataFrame(res)

    item = label.loc[label['subID'] == subId]
    result = pd.concat([item.reset_index(drop=True), HCFvalue.T], axis=1)
    print(result)
    nhcp = pd.concat([nhcp,result])

nhcp.to_csv('./hcpFCSfeature.csv', index=False)