import pandas as pd

# 读取 region246_network_Yeo 表格
region_mapping_path = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/region246_network_Yeo.csv'
region_mapping_df = pd.read_csv(region_mapping_path)

# 提取 regions 和 Yeo_7network 列，建立映射
region_to_network = region_mapping_df.set_index('regions')['Yeo_7network'].to_dict()
print(region_to_network)

# 读取 subtype1_2_Z8w_HAMD_8w 表格
subtype_data_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/Longitudinal/subtype1_2_Z8w_HAMD_8w.csv'
subtype_data_df = pd.read_csv(subtype_data_path)

# # 找到从 A8m_R 开始的列
data_of_interest = subtype_data_df.iloc[:, 6:]

# 建立 Yeo 7 网络的数据结构
network_data = {network: [] for network in set(region_to_network.values())}
print(network_data)

# 将数据分配到对应的 Yeo 7 网络
for column in data_of_interest.columns:
    #region_name = column.split('_')[0]  # 假设列名包含脑区名作为前缀
    region_name = column
    if region_name in region_to_network:
        network = region_to_network[region_name]
        network_data[network].append(data_of_interest[column])

# 计算每个网络中的脑区求和和平均值
network_averages = {}
for network, data_list in network_data.items():
    print(data_list)
    if data_list:  # 确保网络中有数据
        network_df = pd.concat(data_list, axis=1)
        print(network_df)
        exit()
        network_sum = network_df.sum(axis=1)
        network_mean = network_sum / len(data_list)
        network_averages[network] = network_mean

# 将结果保存为 DataFrame
result_df = pd.DataFrame(network_averages)
result_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/Longitudinal/network_level_averages.csv'
result_df.to_csv(result_path, index=False)

print(f"计算完成，结果已保存到 {result_path}")
