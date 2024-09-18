import glob
import pandas as pd
datapath = glob.glob('/Volumes/QCI/HCP_Struc/hcp_res/*/*_SurfArea.csv')


# 读取第一个 CSV 文件，获取列名
first_file = pd.read_csv(datapath[0])
print(first_file)

columns = list(first_file.iloc[0,:])

# 创建一个空的 DataFrame，用于存储拼接后的数据
concatenated_data = pd.DataFrame(columns=columns)

# 拼接每个 CSV 文件的数据
for file in datapath:
    data = pd.read_csv(file, header=1)  # 从第二行开始读取数据
    concatenated_data = pd.concat([concatenated_data, data], axis=0, ignore_index=True)

# 打印拼接后的数据
print(concatenated_data)
concatenated_data.to_csv('./HCPSurfArea.csv')
