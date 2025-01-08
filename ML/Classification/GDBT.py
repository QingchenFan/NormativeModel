import numpy as np
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.ensemble import BaggingClassifier, GradientBoostingClassifier
import pandas as pd
from sklearn.metrics import r2_score, make_scorer, accuracy_score, cohen_kappa_score

Data = pd.read_csv("/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/AllMDD_FirstEpisode.csv")


# all Regions feature
brainRegion = Data.columns.tolist()
del brainRegion[:2]

x_data = np.array(Data[brainRegion])

y_label = np.array(Data['FirstEpisode'])

kf = KFold(n_splits=5, shuffle=True, random_state=6)

acc_res = []
kappa_res = []
for train_index, test_index in kf.split(x_data):

    # split data
    X_train, X_test = x_data[train_index, :], x_data[test_index, :]
    y_train, y_test = y_label[train_index], y_label[test_index]


    # Model
    # GBDT
    clf = GradientBoostingClassifier(n_estimators=100, max_depth=1, random_state=0)

    # 网格交叉验证
    cv_times = 5  # inner
    param_grid = {
        'learning_rate': [1.0, 0.6, 0.1],
    }
    predict_model = GridSearchCV(clf, param_grid, scoring='accuracy', verbose=6, cv=cv_times)

    predict_model.fit(X_train, y_train)
    best_model = predict_model.best_estimator_
    # # weight
    # feature_weight = np.zeros([np.shape(X_train)[1], 1])
    # for i, j in enumerate(predict_model.best_estimator_.estimators_):
    #     # print('第{}个模型的系数{}'.format(i, j.coef_))
    #     # test.to_csv('test_'+str(epoch)+'_'+str(i)+'.csv')
    #     feature_weight = np.add(j.coef_, feature_weight)
    #
    # num = len(predict_model.best_estimator_.estimators_)
    # feature_weight_mean = feature_weight / num
    # print('--feature_weight_mean--\n', feature_weight_mean)
    # feature_weight_res = np.add(feature_weight_mean, feature_weight_res)  # sum = sum + 1
    #

    Predict_Score = best_model.predict(X_test)
    # print('-Predict_Score-', Predict_Score)
    # print('-y_test-', y_test)

    acc = accuracy_score(y_test, Predict_Score)
    print('-acc-', acc)
    acc_res.append(float("%.2f" % (acc)))
    kappa = cohen_kappa_score(np.array(y_test).reshape(-1, 1), np.array(Predict_Score).reshape(-1, 1))
    print('-kappa = %.2f:' % (kappa))
    kappa_res.append(kappa)

print('Result: acc=%.3f, kappa=%.3f ' % (np.mean(acc_res), np.mean(kappa_res)))