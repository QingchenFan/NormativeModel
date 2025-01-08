import nibabel as nib
import numpy as np
from scipy.io import savemat
import pandas as pd

# 模板文件路径
template_path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.BN_Atlas.32k_fs_LR.dlabel.nii'
template = template_path
template = nib.load(template)
label=template.get_fdata()
label[label > 210] -= 210


# 加载 CSV 文件
csv_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/hbr_estimate_GrayVol246_ResSum.csv'
weight_data = pd.read_csv(csv_path)

# 读取 结果指标 列，可以是SMSE\MSLL
smse_values = weight_data['SMSE'].values

# 创建一个新的数组用于存储映射值
mapped_data = np.zeros_like(label)


for i in range(1, 211):
    index = np.where(label == i)

    mapped_data[index] = smse_values[i - 1]

# 检查映射后的数据形状
print("Mapped data shape:", mapped_data.shape)

# 创建 dscalar.nii 文件
scalar_axis = nib.cifti2.cifti2_axes.ScalarAxis(['SMSE'])
brain_model_axis = template.header.get_axis(1)
scalar_header = nib.cifti2.Cifti2Header.from_axes((scalar_axis, brain_model_axis))
scalar_img = nib.Cifti2Image(mapped_data, header=scalar_header)
scalar_img.to_filename('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/SMSE.dscalar.nii')

