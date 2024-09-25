import nibabel as nib
import numpy as np

import pandas as pd

# 模板文件路径
template_path = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_17Networks_order.dlabel.nii'

# 加载 dlabel.nii 模板文件
template_image = nib.load(template_path)
template_data = template_image.get_fdata()
print("Template data shape:", template_data.shape)

# 加载 CSV 文件
csv_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0906/StaResults/GrayVol_ResSum.csv'
weight_data = pd.read_csv(csv_path)

# 读取 结果指标 列，可以是SMSE\MAE
smse_values = weight_data['MAE'].values

# 创建一个新的数组用于存储映射值
mapped_data = np.zeros_like(template_data)

# 映射 SMSE_estimate 值到模板的 400 个脑区
for i in range(1, 401):
    index = np.where(template_data == i)

    mapped_data[index] = smse_values[i - 1]

# 检查映射后的数据形状
print("Mapped data shape:", mapped_data.shape)

# 创建 dscalar.nii 文件
scalar_axis = nib.cifti2.cifti2_axes.ScalarAxis(['MAE'])
brain_model_axis = template_image.header.get_axis(1)
scalar_header = nib.cifti2.Cifti2Header.from_axes((scalar_axis, brain_model_axis))
scalar_img = nib.Cifti2Image(mapped_data, header=scalar_header)
scalar_img.to_filename('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0906/StaResults/MAE_estimate.dscalar.nii')

