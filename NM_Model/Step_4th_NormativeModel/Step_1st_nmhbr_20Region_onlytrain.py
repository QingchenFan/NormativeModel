import os
import pandas as pd
import pcntoolkit as ptk
import numpy as np
import pickle
from matplotlib import pyplot as plt




allHC_tr = pd.read_csv('Data/allHC_tr.csv')
allHC_te = pd.read_csv('Data/allHC_te.csv')

anding_tr = pd.read_csv('Data/allHC_anding_tr.csv')
anding_te = pd.read_csv('Data/allHC_anding_te.csv')
#--要训练的脑区

idps = ['LH_Vis_1','LH_Default_PFC_12','LH_DorsAttn_PrCv_1','LH_Default_pCunPCC_5','LH_SalVentAttn_TempOcc_1',
        'LH_Limbic_OFC_1','LH_Limbic_TempPole_5','LH_Cont_Par_3','LH_Cont_pCun_2','LH_Default_Temp_6',
        'RH_Vis_8','RH_Vis_18','RH_SomMot_3','RH_SomMot_15','RH_SomMot_30','RH_DorsAttn_Post_2',
        'RH_DorsAttn_Post_12','RH_SalVentAttn_Med_5','RH_Limbic_OFC_3','RH_Cont_Par_1'
        ]

# --构建模型的x、y

pro_dir = '/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/Result/'
if not os.path.isdir(pro_dir):
    os.mkdir(pro_dir)
os.chdir(pro_dir)
pro_dir = os.getcwd()

X_train = (allHC_tr['age'] / 100).to_numpy(dtype=float)
# print(X_train)
Y_train = allHC_tr[idps].to_numpy(dtype=float)
# print(Y_train)
batch_effects_train = allHC_tr[['sitenum']].to_numpy(dtype=int)

with open('X_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_train), file)
with open('Y_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_train), file)
with open('trbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_train), file)

X_test = (allHC_te['age'] / 100).to_numpy(dtype=float)
Y_test = allHC_te[idps].to_numpy(dtype=float)

batch_effects_test = allHC_te[['sitenum']].to_numpy(dtype=int)
with open('X_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_test), file)
with open('Y_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_test), file)
with open('tsbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_test), file)


# a simple function to quickly load pickle files
def ldpkl(filename: str):
    with open(filename, 'rb') as f:
        return pickle.load(f)


# --生成对应路径，方便传入参数
respfile = os.path.join(pro_dir,'Y_train.pkl')  # measurements  (eg cortical thickness) of the training samples (columns: the various features/ROIs, rows: observations or subjects)
covfile = os.path.join(pro_dir,'X_train.pkl')  # covariates (eg age) the training samples (columns: covariates, rows: observations or subjects)
testrespfile_path = os.path.join(pro_dir, 'Y_test.pkl')  # measurements  for the testing samples
testcovfile_path = os.path.join(pro_dir, 'X_test.pkl')  # covariate file for the testing samples

trbefile = os.path.join(pro_dir,'trbefile.pkl')  # training batch effects file (eg scanner_id, gender)  (columns: the various batch effects, rows: observations or subjects)
tsbefile = os.path.join(pro_dir, 'tsbefile.pkl')  # testing batch effects file

output_path = os.path.join(pro_dir, 'Models/')  # output path, where the models will be written

log_dir = os.path.join(pro_dir, 'log/')
if not os.path.isdir(output_path):
    os.mkdir(output_path)
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
outputsuffix = '_estimate'
# --训练模型
ptk.normative.estimate(covfile=covfile,
                       respfile=respfile,
                       tsbefile=tsbefile,
                       trbefile=trbefile,
                       inscaler='standardize',
                       outscaler='standardize',
                       linear_mu='True',
                       random_intercept_mu='True',
                       centered_intercept_mu='True',
                       alg='hbr',
                       log_path=log_dir,
                       binary=True,
                       output_path=output_path,
                       testcov=testcovfile_path,
                       testresp=testrespfile_path,
                       outputsuffix=outputsuffix,
                       savemodel=True)
# ----------------------------微调模型------------------------------------
# --构建模型的x、y
X_adapt = (anding_tr['age'] / 100).to_numpy(dtype=float)
Y_adapt = anding_tr[idps].to_numpy(dtype=float)
# batch_effects_adapt = icbm_tr[['sitenum','sex']].to_numpy(dtype=int)
batch_effects_adapt = anding_tr[['sitenum']].to_numpy(dtype=int)

with open('X_adaptation.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_adapt), file)
with open('Y_adaptation.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_adapt), file)
with open('adbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_adapt), file)

# Test data (new dataset)
X_test_txfr = (anding_te['age'] / 100).to_numpy(dtype=float)
Y_test_txfr = anding_te[idps].to_numpy(dtype=float)
# batch_effects_test_txfr = icbm_te[['sitenum','sex']].to_numpy(dtype=int)
batch_effects_test_txfr = anding_te[['sitenum']].to_numpy(dtype=int)

with open('X_test_txfr.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_test_txfr), file)
with open('Y_test_txfr.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_test_txfr), file)
with open('txbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_test_txfr), file)

respfile = os.path.join(pro_dir, 'Y_adaptation.pkl')              #  train y
covfile = os.path.join(pro_dir, 'X_adaptation.pkl')               #  train x
testrespfile_path = os.path.join(pro_dir, 'Y_test_txfr.pkl')      #  test y
testcovfile_path = os.path.join(pro_dir, 'X_test_txfr.pkl')       #  test x
trbefile = os.path.join(pro_dir, 'adbefile.pkl')                  #  train batch effects
tsbefile = os.path.join(pro_dir, 'txbefile.pkl')                  #  test batch effects

log_dir = os.path.join(pro_dir, 'log_transfer/')
output_path = os.path.join(pro_dir, 'Transfer/')
model_path = os.path.join(pro_dir, 'Models/')  # path to the previously trained models


outputsuffix = '_transfer'
# --最终训练模型
yhat, s2, z_scores = ptk.normative.transfer(covfile=covfile,
                                            respfile=respfile,
                                            tsbefile=tsbefile,
                                            trbefile=trbefile,

                                            inscaler='standardize',
                                            outscaler='standardize',
                                            linear_mu='True',
                                            random_intercept_mu='True',
                                            centered_intercept_mu='True',
                                            model_path=model_path,
                                            alg='hbr',
                                            log_path=log_dir,
                                            binary=True,
                                            output_path=output_path,
                                            testcov=testcovfile_path,
                                            testresp=testrespfile_path,
                                            outputsuffix=outputsuffix,
                                            savemodel=True)