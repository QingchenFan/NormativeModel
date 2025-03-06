import numpy as np
import nibabel as nib
import pandas as pd
import scipy.io as sio
from scipy.stats import ttest_ind
import statsmodels.stats.multitest as smm
tpath = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.BN_Atlas.32k_fs_LR.dlabel.nii'
template = tpath
template = nib.load(template)
label=template.get_fdata()
label[label > 210] -= 210
pvalue = pd.read_csv('/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1228-2024122801_test/Step_3th_OutliersCount/Step5_MDDHCCond.csv')
# 显著的 T值 map brain
# data = pvalue['fdr-pvalue-s']
# data = np.where(data > 0.05,np.nan,data)
# cohend map brain
data = pvalue['cohen_d']
for i in range(1, data.shape[0]+1):
    index = np.where(label == i)
    label[:,index] = data[i-1]



scalar_axis = nib.cifti2.cifti2_axes.ScalarAxis(['meanZvalue'])
brain_model_axis = template.header.get_axis(1)
scalar_header = nib.cifti2.Cifti2Header.from_axes((scalar_axis, brain_model_axis))
scalar_img = nib.Cifti2Image(label, header=scalar_header)
scalar_img.to_filename('./Cohend_MDDHC.dscalar.nii')