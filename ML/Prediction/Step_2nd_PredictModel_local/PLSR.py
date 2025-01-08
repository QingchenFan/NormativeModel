#coding: utf-8
import os
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cross_decomposition import PLSRegression

from sklearn.model_selection import GridSearchCV, KFold
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import r2_score, make_scorer
from datetime import datetime
import sys

import statsmodels.formula.api as sm
#import pingouin as pg

def my_scorer(y_true, y_predicted):
    mae = np.mean(np.abs(y_true - y_predicted))

    Predict_Score_new = np.transpose(y_predicted)
    Corr = np.corrcoef(Predict_Score_new, y_true)
    Corr = Corr[0, 1]  #

    error = (1/mae)+Corr
    return error

def LoadData(datapath, labelpath, dimention, covariatespath, Permutation=0):

    data_list = []
    data_files_all = pd.read_csv(datapath)
    data_files_all = np.array(data_files_all.iloc[:,5:])

    # Label
    label_files_all = pd.read_csv(labelpath)
    label = label_files_all[dimention]
    y_label = np.array(label)

    x_data = data_files_all
    # Todo: Covariates
    # #Covariates
    # Covariates = pd.read_csv(covariatespath)
    # Covariates = np.array(Covariates)
    # Covariates = Covariates[:, 1:].astype(float)

    # if do permutation , random data
    if Permutation:
        np.random.shuffle(x_data)

    data_list.append(x_data)
    data_list.append(y_label)
#    data_list.append(Covariates)  # Todo: Covariates
    return data_list

def PLSPrediction_Model(data_list, dimention, weightpath, Permutation, kfold, datamark, outputdatapath, count, Time=1):
    epoch = 0
    #count = '01'
    print('--count--', count)
    outer_results_parR = []
    outer_results_R = []
    outer_results_mae = []
    outer_results_r2 = []

    dataMark = datamark
    x_data = data_list[0]
    y_label = data_list[1]

#    Covariates = data_list[2]  # Todo: Covariates
    feature_weight_res = np.zeros([np.shape(x_data)[1], 1])

    kf = KFold(n_splits=kfold, shuffle=True)
    for train_index, test_index in kf.split(x_data):
        epoch = epoch + 1
        # split data
        X_train, X_test = x_data[train_index, :], x_data[test_index, :]
        y_train, y_test = y_label[train_index], y_label[test_index]
    #   Covariates_train, Covariates_test = Covariates[train_index, :], Covariates[test_index, :] # Todo: Covariates

        normalize = preprocessing.MinMaxScaler()
        subjects_data_train = normalize.fit_transform(X_train)
        subjects_data_test = normalize.transform(X_test)

        #ToolboxCSV_server(outputdatapath, y_train,  Time, 'train_label_bagging_' + dimention + '_' + str(Time) + '_' + str(count)+'_' + str(epoch) + '.csv')

        # if Permutation == 0:
        #    ToolboxCSV_server(outputdatapath, y_test, Time, 'test_label_bagging_' + dimention + '_' + str(Time) + '_'+str(count) + '_' + str(epoch) + '.csv')

        # Model
        # PLS


        # 网格交叉验证
        my_func = make_scorer(my_scorer, greater_is_better=True)
        cv_times = 5  # inner

        param_grid = {
            'n_components': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        }
        predict_model = GridSearchCV(PLSRegression(), param_grid, verbose=6, cv=cv_times)

        predict_model.fit(X_train, y_train)

        best_model = predict_model.best_estimator_


        #weight
        feature_weight = np.zeros([np.shape(X_train)[1], 1])

        feature_weight = np.add(best_model.coef_, feature_weight)


        feature_weight_mean = feature_weight
        # print('--feature_weight_mean--\n', feature_weight_mean)
        feature_weight_res = np.add(feature_weight_mean, feature_weight_res)  # sum = sum + 1


        Predict_Score = best_model.predict(X_test)

        #ToolboxCSV_server(outputdatapath, Predict_Score, Time,'Predict_Score_bagging_' + dimention + '_' + str(Time) + '_' +str(count) + '_' + str(epoch) + '.csv')
        # TODO: Controlling covariates and save parCorr
        # preTrueCovari = {"predict": Predict_Score.flatten(),
        #                  "true": y_test,
        #                  "age": Covariates_test[:, 0],
        #                  "sex": Covariates_test[:, 1],
        #                  "fd": Covariates_test[:, 2]}
        #
        # preTrueCovari = pd.DataFrame(preTrueCovari)
        # resCovari = pg.partial_corr(data=preTrueCovari, x='true', y='predict', covar=['age', 'sex', 'fd'])
        # parCorr = resCovari['r']
        # outer_results_parR.append(parCorr)

        # Don't Controlling covariates and save Corr
        Predict_Score_new = np.transpose(Predict_Score)
        Corr = np.corrcoef(Predict_Score_new, y_test)
        Corr = Corr[0, 1]
        outer_results_R.append(Corr)

        MAE_inv = round(np.mean(np.abs(Predict_Score - y_test)), 4)
        outer_results_mae.append(MAE_inv)

        r2 = r2_score(y_test, Predict_Score_new)

        outer_results_r2.append(r2)
        #TODO :parCorr
  #     print('>parCorr=%.3f,Corr=%.3f, MAE=%.3f, r2=%.3f,est=%.3f, cfg=%s' % (parCorr, Corr, MAE_inv, r2, predict_model.best_score_, predict_model.best_params_))
        print('>Corr=%.3f, MAE=%.3f, r2=%.3f,est=%.3f, cfg=%s' % (Corr, MAE_inv, r2, predict_model.best_score_, predict_model.best_params_))

    feature_weight_res_mean = feature_weight_res / kfold
    feature_weight_file = pd.DataFrame(feature_weight_res_mean)

    if Permutation:
       wpath = weightpath + 'pt/'+str(datetime.now().strftime('%Y_%m_%d'))+'_' + str(Time)
       if not os.path.exists(wpath):
           os.makedirs(wpath)
       feature_weight_file.to_csv(weightpath + 'pt/'+str(datetime.now().strftime('%Y_%m_%d'))+'_'+str(Time)+'/feature_weight_' + str(round(np.mean(outer_results_parR), 2)) + '_'+ str(round(np.mean(outer_results_R), 2)) +
                                  '_'+str(count) + '_' +dimention + '.csv')
    else:
        wpath = weightpath + 'tw/' + str(datetime.now().strftime('%Y_%m_%d')) + '_' + str(Time)
        if not os.path.exists(wpath):
            os.makedirs(wpath)
        feature_weight_file.to_csv(weightpath + 'tw/' + str(datetime.now().strftime('%Y_%m_%d')) + '_' + str(Time) + '/feature_weight_' + str(round(np.mean(outer_results_parR), 2)) + '_' + str(round(np.mean(outer_results_R), 2)) +
                                   '_' + str(count) + '_' + dimention + '.csv')
#    print('Result: Covariates-R=%.3f, R=%.3f ,MAE=%.3f, r2=%.3f' % (np.mean(outer_results_parR), np.mean(outer_results_R), np.mean(outer_results_mae), np.mean(outer_results_r2)))
    # TODO :parCorr Covariates-R=%.3f
    print('Result: R=%.3f ,MAE=%.3f, r2=%.3f' % (np.mean(outer_results_R), np.mean(outer_results_mae), np.mean(outer_results_r2)))

def Controllingcovariates(Covariates, X_train, X_test, Covariates_train, Covariates_test):
    Features_Quantity = np.shape(X_train)[1]
    Covariates_Quantity = np.shape(Covariates)[1] - 1  # Covariates_Quantity = 4 因为有一列subjectkey
    # Controlling covariates from brain data
    df = {}
    for k in np.arange(Covariates_Quantity):
        df['Covariate_' + str(k)] = Covariates_train[:, k + 1]  # k+1 避免取到第一列subjectkey

    # Construct formula
    Formula = 'Data ~ Covariate_0'
    for k in np.arange(Covariates_Quantity - 1) + 1:
        Formula = Formula + ' + Covariate_' + str(k)  # Formula = Covariate_0 + Covariate_1 + Covariate_2

    # Regress covariates from each brain features
    for k in np.arange(Features_Quantity):
        df['Data'] = X_train[:, k]  # 训练集
        # Regressing covariates using training data
        LinModel_Res = sm.ols(formula=Formula,
                              data=df).fit()  # df{'Data':Subjects_Data_train，'Covariate_0':age,'Covariate_1':sex,'Covariate_2':FD}
        # Using residuals replace the training data
        X_train[:, k] = LinModel_Res.resid  # 回归后的结果(新特征，残差)
        # Calculating the residuals of testing data by applying the coeffcients of training data
        Coefficients = LinModel_Res.params
        X_test[:, k] = X_test[:, k] - Coefficients[0]
        for m in np.arange(Covariates_Quantity):  # [0, 1 , 2 ]
            X_test[:, k] = X_test[:, k] - Coefficients[m + 1] * Covariates_test[:, m + 1]
    return X_train, X_test


def ToolboxCSV_server(savePath, listbox, Time, filename='filename.csv'):
    print('-toolbox-', savePath+filename)
    sp = savePath +''+str(datetime.now().strftime('%Y_%m_%d')) + '_' + str(Time)
    if not os.path.exists(sp):
        os.makedirs(sp)
    file = open(sp+'/'+filename, mode='w')
    for tra in listbox:
        if(isinstance(tra,str)):
          file.write(tra)
          file.write('\n')
        else:
            file.write(str(tra))
            file.write('\n')


if __name__ == '__main__':
    datapath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/Longitudinal/PDND_Zvalue_HAMD_52w.csv'
    labelpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/Longitudinal/PDND_Zvalue_HAMD_52w.csv'
    dimention = 'HAMD17_52w'
    outputdatapath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/Longitudinal/Predict/'

    weightpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/Longitudinal/Predict/mw'

    data_list = LoadData(datapath, labelpath, dimention, covariatespath=0)
    for i in range(1, 102):
        PLSPrediction_Model(data_list, dimention, weightpath, Permutation=0, kfold=10, datamark='HAMD', outputdatapath=outputdatapath, count=i, Time=2)