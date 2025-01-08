import glob
import pandas as pd
# TODO: 对 BN210+BN subcortical36 的 csv文件进行拼接
datapath = glob.glob('/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature_Brainnetom/*/*GrayVolSubcortical.csv')
# 读取第一个 CSV 文件，获取列名
first_file = pd.read_csv(datapath[0])

columns = list(first_file.iloc[0,:])
print(len(columns))

# 创建一个空的 DataFrame，用于存储拼接后的数据
concatenated_data = pd.DataFrame(columns=columns)
print(concatenated_data)
# 拼接每个 CSV 文件的数据
for file in datapath:
    print(file)
    data = pd.read_csv(file, header=1)  # 从第二行开始读取数据
    print(data)
    print(data.shape)
    concatenated_data = pd.concat([concatenated_data, data], axis=0, ignore_index=True)


# 打印拼接后的数据
concatenated_data.to_csv('./Data135_MDD_GrayVol_all246.csv')
