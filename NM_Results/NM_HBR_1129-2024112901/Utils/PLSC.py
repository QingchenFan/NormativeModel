import numpy as np
import pandas as pd
from sklearn.cross_decomposition import PLSCanonical
from scipy.stats import pearsonr, zscore
from sklearn.utils import shuffle

# 加载数据
alldata = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/subtype1_ZvalueHAMD.csv')
alldata = np.array(alldata)

# 分离 X 和 Y
X = alldata[:, 1:225]
Y = alldata[:, 225:]

# 标准化

Y = alldata[:, 225:]
Y = np.array(Y, dtype=np.float64)
Y = zscore(Y, axis=0)

# 设置参数
n_components = 10
n_permutations = 1000  # 置换次数

# 构建和拟合 PLS 模型
plsc = PLSCanonical(n_components=n_components)
plsc.fit(X, Y)

# 转换 X 和 Y
X_train_r, Y_train_r = plsc.transform(X, Y)

a = plsc.explained_variance_
print(a)
# 计算原始相关性
original_corr = np.corrcoef(X_train_r[:, 0], Y_train_r[:, 0])[0, 1]

# 置换检验
permuted_corrs = []
for i in range(n_permutations):
    print('---',i,'---')
    # 随机置换 Y
    Y_permuted = shuffle(Y, random_state=i)
    plsc.fit(X, Y_permuted)
    X_perm_r, Y_perm_r = plsc.transform(X, Y_permuted)
    perm_corr = np.corrcoef(X_perm_r[:, 0], Y_perm_r[:, 0])[0, 1]
    permuted_corrs.append(perm_corr)

# 计算 p 值
permuted_corrs = np.array(permuted_corrs)
p_value = np.mean(np.abs(permuted_corrs) >= np.abs(original_corr))

# 输出结果
print(f"原始相关性: {original_corr}")
print(f"p 值: {p_value}")

