import nibabel as nib
import numpy as np
from scipy import io
from scipy.io import savemat
import pandas as pd

# 加载 CSV 文件
csv_path = '/Users/qingchen/Documents/code/NormativeModel_Result/Result_GrayVol_10K_HCMDD_0826/Step_5th_Subtype/step4_group_subtype1_Regionmean.csv'
weight_data = pd.read_csv(csv_path)

# 读取 SMSE_estimate 列
mean_Zvalues = weight_data.iloc[0:400,1].values

print("values shape:", mean_Zvalues)
# 模板文件路径
template_path = '/Users/qingchen/Documents/code/Data/FC/Schaefer2018_400Parcels_17Networks_order.dlabel.nii'

# 加载 dlabel.nii 模板文件
template_image = nib.load(template_path)
template_data = template_image.get_fdata()
print("Template data shape:", template_data.shape)

#构建dscalar文件,
# 创建一个新的数组用于存储映射值
mapped_data = np.zeros_like(template_data)

# 找到脑区对应的索引
Regionscsv_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/GrayVol_ResSum.csv'
Regions_data = pd.read_csv(Regionscsv_path)
region = Regions_data['Regions'][0:400]
schaefer = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0826/StaResults/atlas-Schaefer2018v0143_desc-400ParcelsAllNetworks_dseg.csv')
for i,regionname in enumerate(region):
    print('i - ',i)
    print('regionname - ',regionname)
    Regionindex = schaefer.loc[schaefer['label_17network'] == regionname]['index_17network'].values[0]
    print('Regionindex - ',Regionindex)
    Regionindexs = np.where(template_data == Regionindex)
    print('mean_Zvalues',mean_Zvalues[i])
    mapped_data[Regionindexs] = mean_Zvalues[i]

# 检查映射后的数据形状
print("Mapped data shape:", mapped_data.shape)

# 创建 dscalar.nii 文件
scalar_axis = nib.cifti2.cifti2_axes.ScalarAxis(['meanZvalue'])
brain_model_axis = template_image.header.get_axis(1)
scalar_header = nib.cifti2.Cifti2Header.from_axes((scalar_axis, brain_model_axis))
scalar_img = nib.Cifti2Image(mapped_data, header=scalar_header)
scalar_img.to_filename('./subtype1_xxxMeanDeviation.dscalar.nii')

