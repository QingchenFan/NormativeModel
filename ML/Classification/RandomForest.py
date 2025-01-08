from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.metrics import cohen_kappa_score
import numpy as np
import pandas as pd
from sklearn import svm


Data = pd.read_csv("/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/AllMDD_FirstEpisode.csv")



# all Regions feature
brainRegion = Data.columns.tolist()
del brainRegion[:2]

x_data = np.array(Data[brainRegion])

y_label = np.array(Data['FirstEpisode'])

kf = KFold(n_splits=2,shuffle=True)
acc_res = []
kappa_res = []
for train_index, test_index in kf.split(x_data):

    # split data
    X_train, X_test = x_data[train_index, :], x_data[test_index, :]

    y_train, y_test = y_label[train_index], y_label[test_index]

    rf = RandomForestClassifier()
    # param_grid = {
    #     'n_estimators': [50, 100, 200],
    #     'max_depth': [10, 15, 20, 30],
    #     'min_samples_split': [2, 5, 10]
    # }
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['sqrt', 'log2', None]
    }
    predict_model = grid_search = GridSearchCV(estimator=rf, param_grid=param_grid, cv=2, verbose=6,scoring='accuracy')

    predict_model.fit(X_train, y_train)
    best_model = predict_model.best_estimator_
    # 预测并计算新结果
    y_pred_bal = best_model.predict(X_test)

    classification_report_bal = classification_report(y_test, y_pred_bal)



    #print('-Predict_Score-', Predict_Score)
    print('y_test:',y_test)
    print('Predict_Score:',y_pred_bal)

    acc = accuracy_score(y_test, y_pred_bal)
    print('-acc = %.2f:' %(acc))
    acc_res.append(float("%.2f"%(acc)))

    kappa = cohen_kappa_score(np.array(y_test).reshape(-1, 1), np.array(y_pred_bal).reshape(-1, 1))
    print('-kappa = %.2f:' %(kappa))
    kappa_res.append(kappa)

    # 通过测试集的预测结果
    # 打印出三种评估指标的分类报告进行模型评估
    #print(metrics.classification_report(y_test, Predict_Score))

print(acc_res)
print('Result: acc = %.3f, kappa = %.3f ' % (np.mean(acc_res), np.mean(kappa_res)))