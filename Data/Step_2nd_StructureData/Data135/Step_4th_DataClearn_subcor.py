import glob
import pandas as pd

# 获取所有 *_GrayVol.csv 文件的路径
datapath = glob.glob('/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature_Brainnetom/*/*_GrayVol.csv')

# 需要提取的列名列表
columns_to_extract = [
    "Left-Thalamus", "Left-Caudate", "Left-Putamen", "Left-Pallidum",
    "Left-Hippocampus", "Left-Amygdala", "Left-Accumbens-area",
    "Right-Thalamus", "Right-Caudate", "Right-Putamen", "Right-Pallidum",
    "Right-Hippocampus", "Right-Amygdala", "Right-Accumbens-area"
]

# 读取第一个 CSV 文件，获取列名
first_file = pd.read_csv(datapath[0])
columns = list(first_file.iloc[0,:])
# 在列名中添加需要提取的列名
columns.extend(columns_to_extract)

# 创建一个空的 DataFrame，用于存储拼接后的数据
concatenated_data = pd.DataFrame(columns=columns)

# 拼接每个 CSV 文件的数据
for file in datapath:
    # 获取文件夹路径
    folder_path = '/'.join(file.split('/')[:-1])
    #  方便 246 模版
    subID = file.split('/')[-2]
    folder_path = '/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature_Schaefer400/' + subID

    # 获取对应的 subcortialvolume.txt 文件路径
    subcortialvolume_file = f"{folder_path}/subcortialvolume.txt"

    # 读取 *_GrayVol.csv 文件
    gray_vol_data = pd.read_csv(file, header=1)
    gray_vol_data = gray_vol_data.iloc[0:1,:]
    # 读取 subcortialvolume.txt 文件
    subcortialvolume_data = pd.read_csv(subcortialvolume_file, delimiter='\t')
    # 提取需要的列
    extracted_data = subcortialvolume_data[columns_to_extract].iloc[0].to_dict()

    # 将提取的列添加到 gray_vol_data 对应的行中
    for column in columns_to_extract:
        gray_vol_data[column] = extracted_data[column]
    # 将数据拼接到 concatenated_data 中
    concatenated_data = pd.concat([concatenated_data, gray_vol_data], axis=0, ignore_index=True)

# 保存拼接后的数据到新的 CSV 文件
concatenated_data.to_csv('./Data135MDDGrayVol_246.csv', index=False)
