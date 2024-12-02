import nibabel as nib
import numpy as np
import scipy.io as sio
import pandas as pd

# 模板文件路径
template_path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.BN_Atlas.32k_fs_LR.dlabel.nii'
template = template_path
template = nib.load(template)
label=template.get_fdata()
label[label > 210] -= 210

# 找到脑区对应的索引
Regionscsv_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1128/StaResults/hbr_estimate_GrayVol246_ResSum.csv'
Regions_data = pd.read_csv(Regionscsv_path)
region = Regions_data['Regions'][0:210]

# 加载 CSV 文件
#csv_path = '/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1128-2024112801/Step_3th_OutliersCount/Step3_Z_AllMDD_NegativeBrainRegionNum.csv'
csv_path = '/Users/qingchen/Documents/code/NormativeModel/NM_Results/NM_HBR_1128-2024112801/Step_3th_OutliersCount/Step3_Z_AllMDD_PositiveBrainRegionNum.csv'

weight_data = pd.read_csv(csv_path)
print(weight_data.shape)

sumRegion = weight_data.iloc[391:392,2:].values

# 创建一个新的数组用于存储映射值
mapped_data = np.zeros_like(label)


for i,regionname in enumerate(region):
    i = i + 1
    index = np.where(label == i)
    mapped_data[index] = sumRegion[0][i] / weight_data.shape[0]
# 检查映射后的数据形状
print("Mapped data shape:", mapped_data.shape)

# 创建 dscalar.nii 文件
scalar_axis = nib.cifti2.cifti2_axes.ScalarAxis(['MAE'])
brain_model_axis = template.header.get_axis(1)
scalar_header = nib.cifti2.Cifti2Header.from_axes((scalar_axis, brain_model_axis))
scalar_img = nib.Cifti2Image(mapped_data, header=scalar_header)

#scalar_img.to_filename('./step4_NegativeBrainRegionNum.dscalar.nii')
scalar_img.to_filename('./step4_PositiveBrainRegionNum.dscalar.nii')

