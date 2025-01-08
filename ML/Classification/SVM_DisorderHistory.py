from sklearn import svm
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import accuracy_score
import numpy as np
import pandas as pd
from sklearn.utils import resample
from sklearn.metrics import accuracy_score, cohen_kappa_score

# 读取数据
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

# -------
# all Regions feature
brainRegion = Data.columns.tolist()
del brainRegion[:2]
print(brainRegion)

x_data = np.array(data_balanced[brainRegion])

y_label = np.array(data_balanced['disorderHistory'])


#
# # 定义超参数网格
# param_grid = {
#     'C': [0.1, 1, 10, 100],   # 惩罚系数
#     'gamma': [0.001, 0.01, 0.1, 1],  # 核函数的gamma参数
# }
#
# # 定义外层和内层交叉验证
# outer_cv = KFold(n_splits=5, shuffle=True)  # 外层交叉验证
# inner_cv = KFold(n_splits=5, shuffle=True)  # 内层交叉验证
#
# # 用于存储所有重复的外层验证得分
# all_outer_scores = []
#
# # 设置重复次数
# n_repeats = 101
#
# for repeat in range(n_repeats):
#     # 用于存储本次重复中外层交叉验证的结果
#     outer_scores = []
#
#     for train_idx, test_idx in outer_cv.split(X):
#         # 分割数据
#         X_train, X_test = X[train_idx], X[test_idx]
#         y_train, y_test = y[train_idx], y[test_idx]
#
#         # 定义SVM模型
#         svmmodel = svm.SVC(kernel='linear')
#
#         # 内层网格搜索
#         grid_search = GridSearchCV(
#             estimator=svmmodel,
#             param_grid=param_grid,
#             cv=inner_cv,
#             scoring='accuracy',
#             n_jobs=-1
#         )
#         grid_search.fit(X_train, y_train)
#
#         # 使用最佳参数的模型在外层测试集上进行预测
#         best_model = grid_search.best_estimator_
#         y_pred = best_model.predict(X_test)
#         test_score = accuracy_score(y_test, y_pred)
#         outer_scores.append(test_score)
#
#         # 打印每次外层交叉验证的结果
#         print(f"外层测试集得分 (重复 {repeat + 1}, 外层得分): {test_score:.4f}")
#         print(f"最佳参数: {grid_search.best_params_}")
#
#     # 将本次重复的外层交叉验证结果添加到所有得分列表中
#     all_outer_scores.append(outer_scores)
#
# # 计算每次重复的外层交叉验证的中位数
# median_scores = [np.median(scores) for scores in all_outer_scores]
# print()
# # 输出最终结果：101次重复的中位数
# print("\n嵌套交叉验证 101 次重复的中位数准确率: {:.4f}".format(np.median(median_scores)))
n_repeats = 101
FinalRes = []
for repeat in range(n_repeats):
    kf = KFold(n_splits=5, shuffle=True)
    inner_cv = 5
    outer_scores = []
    acc_res = []
    kappa_res = []
    for train_index, test_index in kf.split(x_data):
        # split data
        X_train, X_test = x_data[train_index, :], x_data[test_index, :]
        y_train, y_test = y_label[train_index], y_label[test_index]

        # 定义SVM模型
        svmmodel = svm.SVC(kernel='linear')
        param_grid = {
                'C': [0.1, 1, 10, 100],   # 惩罚系数
                'gamma': [0.001, 0.01, 0.1, 1],  # 核函数的gamma参数
            }
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

        acc = accuracy_score(y_test, y_pred)
        print('-acc = %.2f:' %(acc))
        acc_res.append(float("%.2f"%(acc)))

        kappa = cohen_kappa_score(np.array(y_test).reshape(-1, 1), np.array(y_pred).reshape(-1, 1))
        print('-kappa = %.2f:' % (kappa))
        kappa_res.append(kappa)

    print('Result: acc=%.3f, kappa=%.3f ' % (np.mean(acc_res), np.mean(kappa_res)))
    FinalRes.append(np.mean(acc_res))
print(len(FinalRes))
print('Final Result: acc=%.3f' % (np.median(FinalRes)))
