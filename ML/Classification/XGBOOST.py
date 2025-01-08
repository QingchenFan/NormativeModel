from sklearn.metrics import accuracy_score, cohen_kappa_score
from sklearn.model_selection import train_test_split, KFold
from sklearn.model_selection import GridSearchCV
import xgboost as xgb
import numpy as np
import pandas as pd
Data = pd.read_csv("/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/"
                   "AllMDD_FirstEpisode_xg.csv")


# all Regions feature
brainRegion = Data.columns.tolist()
del brainRegion[:2]

x_data = np.array(Data[brainRegion])

y_label = np.array(Data['FirstEpisode'])

acc_res = []
kappa_res = []
kf = KFold(n_splits=5, shuffle=True, random_state=6)
for train_index, test_index in kf.split(x_data):
    # split data
    X_train, X_test = x_data[train_index, :], x_data[test_index, :]
    y_train, y_test = y_label[train_index], y_label[test_index]

    # Model
    Hyper_param = {'max_depth': range(3, 5, 10),
                   'learning_rate': [0.01, 0.05, 0.08, 0.1, 0.12],
                   }

    predict_model = GridSearchCV(estimator=xgb.XGBClassifier(booster='gbtree',
                                                            n_estimators=100,
                                                            verbosity=0,
                                                            objective="binary:logistic",
                                                            ),
                                 param_grid=Hyper_param,
                                 scoring='accuracy',
                                 verbose=6,
                                 cv=5)
    predict_model.fit(X_train, y_train)

    Predict_Score = predict_model.predict(X_test)
    #print('-Predict_Score-', Predict_Score)
    #print('-y_test-', y_test)

    acc = accuracy_score(y_test, Predict_Score)
    print('-acc = %.2f:' %(acc))
    acc_res.append(float("%.2f"%(acc)))

    kappa = cohen_kappa_score(np.array(y_test).reshape(-1, 1), np.array(Predict_Score).reshape(-1, 1))
    print('-kappa = %.2f:' % (kappa))
    kappa_res.append(kappa)
print('Result: acc=%.3f, kappa=%.3f ' % (np.mean(acc_res), np.mean(kappa_res)))
