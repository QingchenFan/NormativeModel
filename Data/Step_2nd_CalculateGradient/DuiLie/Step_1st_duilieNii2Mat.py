import os
import numpy as np
import nibabel as nib
import glob
from scipy.io import savemat

FCpath = '/Volumes/QCII/duilie_processed/duilie_HC_xcpd/*/func/*ap*4S456*.pconn.nii'

file = glob.glob(FCpath)

for i in file:
    subID = i.split('/')[5]
    print(subID)
    FCData = nib.load(i).get_fdata()
    FCData = FCData[0:400,0:400]

    newpath = '/Volumes/QCI/NormativeModel/DuiLie/HC/DuiLie_Schaefer400FC_mat/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    savemat(newpath +'/'+ subID + '_Schaefer400FC.mat', {'data':FCData})
