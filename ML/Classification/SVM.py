
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.metrics import cohen_kappa_score
import numpy as np
import pandas as pd
from sklearn import svm
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

kf = KFold(n_splits=5, shuffle=True)
acc_res = []
kappa_res = []
for train_index, test_index in kf.split(x_data):

    # split data
    X_train, X_test = x_data[train_index, :], x_data[test_index, :]

    y_train, y_test = y_label[train_index], y_label[test_index]


    # Model
    svmmodel = svm.SVC(kernel='linear')

    svmmodel.fit(X_train, y_train)
    t_score = svmmodel.score(X_train, y_train)
    #print('t_score', t_score)
    Predict_Score = svmmodel.predict(X_test)
    #print('-Predict_Score-', Predict_Score)
    print('y_test:', y_test)
    print('Predict_Score:', Predict_Score)

    acc = accuracy_score(y_test, Predict_Score)
    print('-acc = %.2f:' %(acc))
    acc_res.append(float("%.2f"%(acc)))

    kappa = cohen_kappa_score(np.array(y_test).reshape(-1, 1), np.array(Predict_Score).reshape(-1, 1))
    print('-kappa = %.2f:' %(kappa))
    kappa_res.append(kappa)


    # 通过测试集的预测结果
    # 打印出三种评估指标的分类报告进行模型评估
    #print(metrics.classification_report(y_test, Predict_Score))

print(acc_res)
print('Result: acc = %.3f, kappa = %.3f ' % (np.mean(acc_res), np.mean(kappa_res)))