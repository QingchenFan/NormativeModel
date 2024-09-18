import nibabel as nib
import glob
'''
    
    sub-693461 无LR数据
'''
from scipy.io import savemat

FCpath = '/Volumes/QCI/HCPData/HCP_Schaefer400FC/*'

file = glob.glob(FCpath)

for i in file:
    subId = i[-10:]
    Fcpath = glob.glob(i+'/*-LR*')
    if len(Fcpath) == 0:
        print('》》》》',i)
        continue
    FCData = nib.load(Fcpath[0]).get_fdata()
    savemat('/Volumes/QCI/HCPData/HCP_Schaefer400FC_mat/' + subId + '_Schaefer400FC.mat', {'data':FCData})