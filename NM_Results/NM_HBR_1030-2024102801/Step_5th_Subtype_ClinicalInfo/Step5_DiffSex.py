import numpy as np
from scipy.stats import chi2_contingency

# 构建观测频数的二维数组，对应列联表中的数据
observed = np.array([[30, 20],
                     [40, 30]])

# 进行卡方检验
chi2, p, dof, expected = chi2_contingency(observed)

print("卡方统计量:", chi2)
print("p值:", p)
print("自由度:", dof)
print("期望频数:\n", expected)