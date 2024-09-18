import glob
import pandas as pd

# 获取所有 *_GrayVol.csv 文件的路径
datapath = glob.glob('/Volumes/QCI/NormativeModel/Data135/HC/Strufeature/*/*_GrayVol.csv')

# 需要提取的列名列表
columns_to_extract = [
    "Left-Thalamus", "Left-Caudate", "Left-Putamen", "Left-Pallidum",
    "Left-Hippocampus", "Left-Amygdala", "Left-Accumbens-area",
    "Right-Thalamus", "Right-Caudate", "Right-Putamen", "Right-Pallidum",
    "Right-Hippocampus", "Right-Amygdala", "Right-Accumbens-area"
]

# 创建一个空的 DataFrame，用于存储拼接后的数据
concatenated_data = pd.DataFrame()

# 拼接每个 CSV 文件的数据
for file in datapath:
    # 获取文件夹路径
    folder_path = '/'.join(file.split('/')[:-1])
    # 获取对应的 subcortialvolume.txt 文件路径
    subcortialvolume_file = f"{folder_path}/subcortialvolume.txt"

    # 读取 *_GrayVol.csv 文件
    gray_vol_data = pd.read_csv(file, header=0)

    # 读取 subcortialvolume.txt 文件
    subcortialvolume_data = pd.read_csv(subcortialvolume_file, delimiter='\t')

    # 提取需要的列
    extracted_data = subcortialvolume_data[columns_to_extract].iloc[0]

    # 将提取的列添加到 gray_vol_data 对应的行中
    for column in columns_to_extract:
        gray_vol_data[column] = extracted_data[column]

    # 将数据拼接到 concatenated_data 中
    concatenated_data = pd.concat([concatenated_data, gray_vol_data], axis=0, ignore_index=True)

# 获取最终的列名
final_columns = list(concatenated_data.columns)

# 保存拼接后的数据到新的 CSV 文件，确保第一行为列名
concatenated_data.to_csv('./Data135HCGrayVol.csv', header=final_columns, index=False)

print("数据已成功拼接并保存到 Data135HCGrayVol.csv")
