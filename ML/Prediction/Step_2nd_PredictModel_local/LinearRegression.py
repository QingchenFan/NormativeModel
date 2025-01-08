import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn.metrics import make_scorer
from scipy.stats import pearsonr
import random

# 使用线性回归进行K折交叉验证，并返回每次的r值
def linear_regression_cv(X, y, n_splits=10, n_runs=101):
    all_r_scores = []
    for _ in range(n_runs):
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=None)
        r_scores = []
        for train_index, test_index in kf.split(X):
            X_train, X_test = X.iloc[train_index], X.iloc[test_index]
            y_train, y_test = y.iloc[train_index], y.iloc[test_index]

            # 训练模型
            model = LinearRegression()
            model.fit(X_train, y_train)

            # 预测
            y_pred = model.predict(X_test)

            # 计算皮尔逊相关系数
            r, _ = pearsonr(y_test, y_pred)
            r_scores.append(r)

        all_r_scores.append(np.mean(r_scores))
    return all_r_scores

# 5. 置换检验
def permutation_test(X, y, res, n_permutations=1000):

    # 存储置换后的r值
    permutation_r_values = []

    for _ in range(n_permutations):
        # 随机打乱目标变量 y
        y_permuted = y.sample(frac=1).reset_index(drop=True)

        # 对置换数据进行一次交叉验证
        permuted_r = linear_regression_cv(X, y_permuted, n_runs=1)
        permutation_r_values.append(permuted_r)

    # 计算p值：原始r值大于等于置换r值的比例
    p_value = np.mean(np.array(permutation_r_values) >= res)

    return p_value
# 读取数据文件
def read_data(file_path):
    return pd.read_csv(file_path)

# 获取特征和目标变量
def get_xy(data):
    # 提取特征（A8m_R之后的列）
    X = data.iloc[:, data.columns.get_loc('A8m_R'):]
    # 提取目标变量
    y = data['HAMD17_52w']
    return X, y

file_path = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/Longitudinal/PDND_Zvalue_HAMD_52w.csv'
data = read_data(file_path)
X, y = get_xy(data)

all_r_scores = linear_regression_cv(X, y)
print(len(all_r_scores))
res = np.median(all_r_scores)
print(res)
pvalue = permutation_test(X, y, res)
print(pvalue)