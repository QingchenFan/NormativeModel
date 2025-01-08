import numpy as np
import pandas as pd
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import KFold
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from scipy.io import savemat
from sklearn.metrics import r2_score

from scipy.stats import pearsonr, zscore
def pls_explained_variance(pls, X, Y_true, do_plot=True):
    r2 = np.zeros(pls.n_components)
    x_transformed = pls.transform(X) # Project X into low dimensional basis
    for i in range(0, pls.n_components):
        Y_pred = (np.dot(x_transformed[:, i][:, np.newaxis],
                         pls.y_loadings_[:, i][:, np.newaxis].T) * pls._y_std
                  + pls._y_mean)
        r2[i] = r2_score(Y_true, Y_pred)
        overall_r2 = r2_score(Y_true, pls.predict(X))  # Use all components together.

    if do_plot:
        component = np.arange(pls.n_components) + 1
        plt.plot(component, r2, '.-')
        plt.xticks(component)
        plt.xlabel('PLS Component #'), plt.ylabel('r2')
        plt.title(f'Summed individual r2: {np.sum(r2):.3f}, '
                  f'Overall r2: {overall_r2:.3f}')
        plt.show()

    return r2, overall_r2
# 加载数据
alldata = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/subtype1_ZvalueHAMD.csv')
alldata = np.array(alldata)

# 分离 X 和 Y
X = alldata[:, 1:225]
# X = np.array(X, dtype=np.float64)
# X = zscore(X, axis=0)

Y = alldata[:, 225:]
Y = np.array(Y, dtype=np.float64)
Y = zscore(Y, axis=0)

# 设置 PLS 参数
n_components = 10
n_permutations = 1000  # 置换次数
pls_scale = True
# 构建和拟合 PLS 模型
pls = PLSRegression(n_components=n_components)
pls.fit(X, Y)

# 提取 X 和 Y 的 loading
x_loadings = pls.x_loadings_
y_loadings = pls.y_loadings_
xloadings = pd.DataFrame(x_loadings).to_csv('./x_loadings.csv')
yloadings = pd.DataFrame(y_loadings).to_csv('./y_loadings.csv')
# 计算 X 和 Y 成分的得分
x_scores = pls.x_scores_
y_scores = pls.y_scores_

# 计算原始数据的相关性
original_corr, _ = pearsonr(x_scores[:, 4], y_scores[:, 4])
print('Correlation between X and Y:', original_corr)
r2, overall_r2 = pls_explained_variance(pls, X, Y, do_plot=False)
print('r2',r2)
print('o_r2',overall_r2)
# 计算每个成分的方差解释度
explained_variance_ratio = []
total_variance = r2_score(Y, pls.predict(X))

for i in range(n_components):
    # 计算单个成分的预测值
    if pls_scale:  # 如果做了标准化
        Y_pred = (
            np.dot(pls.x_scores_[:, i].reshape(-1, 1), pls.y_loadings_[:, i].reshape(-1, 1).T)
            * Y.std(axis=0, ddof=1)[0]
            + Y.mean(axis=0)[0]
        )

    else:  # 未标准化
        Y_pred = (
            np.dot(pls.x_scores_[:, i].reshape(-1, 1), pls.y_loadings_[:, i].reshape(-1, 1).T)
            + Y.mean(axis=0)[0]
        )
    # 计算 R²
    Y_r2 = r2_score(Y, Y_pred)
    explained_variance_ratio.append(Y_r2)

# 将每个成分的解释方差百分比归一化
explained_variance_ratio = np.array(explained_variance_ratio) / total_variance * 100

# 输出每个成分的解释方差百分比
for i, var in enumerate(explained_variance_ratio, 1):
    print(f"成分 {i} 的解释方差百分比：{var:.2f}%")


exit()
# 绘制折线图
plt.figure(figsize=(8, 6))
plt.plot(range(1, n_components + 1), explained_variance_ratio, marker='o', linestyle='-', color='b')
plt.title('Explained Variance per Component')
plt.xlabel('Component')
plt.ylabel('Explained Variance (%)')
plt.grid(True)
plt.xticks(range(1, n_components + 1))  # 设置x轴刻度
#plt.show()

# 置换检验
permuted_corrs = []
for i in range(n_permutations):
    print('-----',i,'-----')
    # 随机置换 Y 的行顺序
    Y_permuted = np.random.permutation(Y)

    # 构建并拟合 PLS 模型
    pls_permuted = PLSRegression(n_components=n_components)
    pls_permuted.fit(X, Y_permuted)

    # 计算置换数据的成分得分
    permuted_x_scores = pls_permuted.x_scores_
    permuted_y_scores = pls_permuted.y_scores_

    # 计算相关性
    permuted_corr, _ = pearsonr(permuted_x_scores[:, 4], permuted_y_scores[:, 4])
    permuted_corrs.append(permuted_corr)

# 计算 p 值
p_value = np.mean([1 if perm_corr >= original_corr else 0 for perm_corr in permuted_corrs])

# 输出结果
print(f"X Loadings Shape: {x_loadings.shape}")
print(f"Y Loadings Shape: {y_loadings.shape}")
print(f"Original Correlation: {original_corr:.4f}")
print(f"Permutation Test P-value: {p_value:.4f}")

# # 可视化置换检验结果
# plt.figure(figsize=(8, 6))
# plt.hist(permuted_corrs, bins=30, alpha=0.7, color='gray', label='Permuted Correlations')
# plt.axvline(original_corr, color='red', linestyle='--', linewidth=2, label='Original Correlation')
# plt.xlabel('Correlation')
# plt.ylabel('Frequency')
# plt.title('Permutation Test for Correlation')
# plt.legend()
# plt.show()
