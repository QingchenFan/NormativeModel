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
FCpath = glob.glob('/Volumes/QCI/NormativeModel/DuiLie/HC/DuiLie_Schaefer400FC_mat/*/*.mat')
print(FCpath)

label = pd.read_csv('/Volumes/QCI/NormativeModel/DuiLie/DLHClabel.csv')
nhcp = pd.DataFrame()
for i in FCpath:
    print(i)
    subId = i.split('/')[7][4:]
    print('---->',subId)

    data = loadmat(i)['data']
    data = arctanh(data)           # fisher-z

    data[np.isinf(data)] = 0       # fisher-z 变换后对角线为inf值，使其变成0，也不会影响FCS值的大小
    data[data < 0.2] = 0           # 卡一个阈值，大于0.2的FCS保留
    res = np.sum(data, axis=0)
    res = calculate_z_scores(res)  # z-score 归一化处理
    HCFvalue = pd.DataFrame(res)

    item = label.loc[label['subID'] == subId]
    print(item)
    result = pd.concat([item.reset_index(drop=True), HCFvalue.T], axis=1)
    print(result)
    nhcp = pd.concat([nhcp,result])

nhcp.to_csv('./DLHCFCSfeature.csv', index=False)

# ------------MDD------------------------
#
# FCpath = glob.glob('/Volumes/QCI/NormativeModel/Data135/MDD/Data135_Schaefer400FC_mat/*/*.mat')
# print(FCpath)
#
# label = pd.read_csv('/Volumes/QCI/NormativeModel/Data135/MDDlabel.csv')
# nhcp = pd.DataFrame()
# for i in FCpath:
#     print(i)
#     subId = i.split('/')[7][4:10]
#     print('---->',subId)
#     data = loadmat(i)['data']
#     data = arctanh(data)
#     data[np.isinf(data)] = 0
#     data[data < 0.2] = 0
#     res = np.sum(data, axis=0)
#     res = calculate_z_scores(res)
#
#     HCFvalue = pd.DataFrame(res)
#
#     item = label.loc[label['subID'] == subId]
#     result = pd.concat([item.reset_index(drop=True), HCFvalue.T], axis=1)
#     print(result)
#     nhcp = pd.concat([nhcp,result])
#
# nhcp.to_csv('./Data13MDDFCSfeature.csv', index=False)