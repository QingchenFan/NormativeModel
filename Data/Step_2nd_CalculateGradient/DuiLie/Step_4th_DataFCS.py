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
# -----------Data135-HC------------------------
# FCpath = glob.glob('/Volumes/QCI/NormativeModel/Data135/HC/Data135_Schaefer400FC_mat/*/*.mat')
# print(FCpath)
#
# label = pd.read_csv('/Volumes/QCI/NormativeModel/Data135/HClabel.csv')
# nhcp = pd.DataFrame()
# for i in FCpath:
#     print(i)
#     subId = i.split('/')[7][4:9]
#     print('---->',subId)
#     data = loadmat(i)['data']
#     data = arctanh(data)
#     data[np.isinf(data)] = 0
#     data[data < 0.2] = 0
#     res = np.sum(data, axis=0)
#     res = calculate_z_scores(res)
#     HCFvalue = pd.DataFrame(res)
#
#     item = label.loc[label['subID'] == subId]
#     result = pd.concat([item.reset_index(drop=True), HCFvalue.T], axis=1)
#     print(result)
#     nhcp = pd.concat([nhcp,result])
#
# nhcp.to_csv('./Data13FCSfeature.csv', index=False)

# ------------MDD------------------------

FCpath = glob.glob('/Volumes/QCI/NormativeModel/Data135/MDD/Data135_Schaefer400FC_mat/*/*.mat')
print(FCpath)

label = pd.read_csv('/Volumes/QCI/NormativeModel/Data135/MDDlabel.csv')
nhcp = pd.DataFrame()
for i in FCpath:
    print(i)
    subId = i.split('/')[7][4:10]
    print('---->',subId)
    data = loadmat(i)['data']
    data = arctanh(data)
    data[np.isinf(data)] = 0
    data[data < 0.2] = 0
    res = np.sum(data, axis=0)
    res = calculate_z_scores(res)

    HCFvalue = pd.DataFrame(res)

    item = label.loc[label['subID'] == subId]
    result = pd.concat([item.reset_index(drop=True), HCFvalue.T], axis=1)
    print(result)
    nhcp = pd.concat([nhcp,result])

nhcp.to_csv('./Data13MDDFCSfeature.csv', index=False)