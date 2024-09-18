import os

import nibabel as nib
import glob
from scipy.io import savemat

FCpath = '/Volumes/QCII/Data135_processed/xcpd_out_mdd/xcp_d/*/func/*ap*4S456*.pconn.nii'

file = glob.glob(FCpath)

for i in file:
    subID = i.split('/')[6]
    print(subID)

    FCData = nib.load(i).get_fdata()
    FCData = FCData[0:400,0:400]

    newpath = '/Volumes/QCI/NormativeModel/Data135/MDD/Data135_Schaefer400FC_mat/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    #savemat(newpath +'/'+ subID + '_Schaefer400FC.mat', {'data':FCData})
