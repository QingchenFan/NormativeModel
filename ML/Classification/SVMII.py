from sklearn import svm
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn.utils import resample

Data = pd.read_csv("/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/"
                   "AllMDD_Zvalue_DisorderHistory.csv")
# ------
# 1. 分离出标签为 0 和标签为 1 的样本
data_0 = Data[Data['disorderHistory'] == 0]
data_1 = Data[Data['disorderHistory'] == 1]

# 2. 从标签为 0 的样本中随机抽取与标签为 1 的样本数量相同的样本
data_0_resampled = resample(data_0,
                            replace=False,  # 不允许重复抽样
                            n_samples=len(data_1),  # 使得样本数与标签为 1 的样本相同
                            random_state=42)  # 设置随机种子以确保可复现

# 3. 合并标签为 1 和随机抽样后的标签为 0 的样本
data_balanced = pd.concat([data_1, data_0_resampled])

# 4. 打乱数据（可以选择是否需要）
data_balanced = data_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

#-------
# all Regions feature
brainRegion = Data.columns.tolist()
del brainRegion[:2]
print(brainRegion)

x_data = np.array(data_balanced[brainRegion])

y_label = np.array(data_balanced['disorderHistory'])

X = np.array(Data[brainRegion])

y = np.array(Data['disorderHistory'])
# 定义超参数网格
param_grid = {
    'C': [0.1, 1, 10, 100],   # 惩罚系数
    'gamma': [0.001, 0.01, 0.1, 1],  # 核函数的gamma参数
}

# 定义外层和内层交叉验证
outer_cv = KFold(n_splits=5, shuffle=True)  # 外层交叉验证
inner_cv = KFold(n_splits=5, shuffle=True)  # 内层交叉验证

# 用于存储外层验证的结果
outer_scores = []

for train_idx, test_idx in outer_cv.split(X):
    # 分割数据
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    # 定义SVM模型
    svmmodel = svm.SVC(kernel='linear')

    # 内层网格搜索
    grid_search = GridSearchCV(
        estimator=svmmodel,
        param_grid=param_grid,
        cv=inner_cv,
        scoring='accuracy',
        n_jobs=-1
    )
    grid_search.fit(X_train, y_train)

    # 使用最佳参数的模型在外层测试集上进行预测
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    test_score = accuracy_score(y_test, y_pred)
    outer_scores.append(test_score)

    # 打印每次外层交叉验证的结果
    print(f"外层测试集得分: {test_score:.4f}")
    print(f"最佳参数: {grid_search.best_params_}")

# 打印嵌套交叉验证的最终结果
print("\n嵌套交叉验证平均准确率: {:.4f} ± {:.4f}".format(np.mean(outer_scores), np.std(outer_scores)))
