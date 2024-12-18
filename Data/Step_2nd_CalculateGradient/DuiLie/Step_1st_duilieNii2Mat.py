import os
import numpy as np
import nibabel as nib
import glob
from scipy.io import savemat

FCpath = '/Volumes/QCII/duilie_processed/duilie_residue_MDD/xcp_d/*/func/*ap*4S456*.pconn.nii'
file = glob.glob(FCpath)
print(file)
for i in file:
    print(i)
    subID = i.split('/')[6]
    print(subID)

    FCData = nib.load(i).get_fdata()
    FCData = FCData[0:400,0:400]

    newpath = '/Users/qingchen/Desktop/residue_data/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    savemat(newpath +'/'+ subID + '_Schaefer400FC.mat', {'data':FCData})
