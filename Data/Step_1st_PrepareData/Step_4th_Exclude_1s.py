import pandas as pd
# step1 统计大于三个标准差 的脑区个数
# 读取数据文件
file_path = '/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstrucIII/nocombat/new_combat/allHC_GrayVol_combat_new.csv'
#file_path = "/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/StructureFeature_246/allstruc/combat/allHC_GrayVol246_combat_temp.csv"
file_path = "/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1216/Feature/AllHC_GrayVol_all246_II.csv"

data = pd.read_csv(file_path)
subid = data['subID']
data = data.iloc[:,4:]


# 计算每个脑区的组均值和标准差
group_means = data.mean(axis=0)
group_stds = data.std(axis=0)


# 定义异常值的标准（均值加减2.698倍标准差）
upper_bound = group_means + 3 * group_stds
lower_bound = group_means - 3 * group_stds

print('upper_bound - ', upper_bound)
print('lower_bound - ', lower_bound)
# 计算每个被试的异常脑区数量
def count_abnormal_regions(row):
    print('row - ',row)
    abnormal_count = ((row > upper_bound) | (row < lower_bound)).sum()
    return abnormal_count


data['abnormal_count'] = data.apply(count_abnormal_regions, axis=1)

data['subID'] = subid
# 输出带有异常脑区数量的数据
output_file_path = './HC_abnormal_counts3st_nocombat.csv'
data.to_csv(output_file_path, index=False)

data.head(), data['abnormal_count'].describe()
