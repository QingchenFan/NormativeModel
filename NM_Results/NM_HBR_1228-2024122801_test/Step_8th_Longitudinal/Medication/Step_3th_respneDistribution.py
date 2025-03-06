import pandas as pd

# 加载用户上传的两个文件
file1_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/Longitudinal/' \
             'subtype1_GrayVol246_Z_AllMDD_HAMD_2w.csv'
file2_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/Longitudinal/' \
             'subtype2_GrayVol246_Z_AllMDD_HAMD_2w.csv'

# 读取CSV文件
subtype1 = pd.read_csv(file1_path)
subtype2 = pd.read_csv(file2_path)

import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency, fisher_exact

# 统计两个亚型的疗效频数
responemark_counts_1 = subtype1['responemark'].value_counts()
responemark_counts_2 = subtype2['responemark'].value_counts()

# 构建列联表
contingency_table = pd.DataFrame({
    "Subtype 1": [responemark_counts_1.get(1, 0), responemark_counts_1.get(0, 0)],
    "Subtype 2": [responemark_counts_2.get(1, 0), responemark_counts_2.get(0, 0)]
}, index=["Effective (1)", "Not Effective (0)"])
print(contingency_table)
# 卡方检验
chi2, p_val, dof, expected = chi2_contingency(contingency_table)
# test_result = "Chi-squared test" if all(expected.flatten() >= 5) else "Fisher's exact test"
#
# # 如果期望频数中有小于5的值，改用Fisher精确检验
# if test_result == "Fisher's exact test":
#     _, p_val = fisher_exact(contingency_table.values)

# 打印统计检验结果
#print(f"Test: {test_result}")
print(f"chi2:{chi2}")
print(f"p-value: {p_val}")
#print(f"Contingency Table:\n{contingency_table}")

# 绘制柱状图
contingency_table.plot(kind='bar', figsize=(8, 6), color=['skyblue', 'salmon'])

# 图形美化
plt.title('Distribution of Effectiveness by Subtype', fontsize=16)
plt.xlabel('Effectiveness', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.legend(title='Subtype', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 展示图形
plt.tight_layout()
#plt.show()