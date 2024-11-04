import os
import pandas as pd
import pcntoolkit as ptk
import numpy as np
import pickle

# # a simple function to quickly load pickle files
def ldpkl(filename: str):
    with open(filename, 'rb') as f:
        return pickle.load(f)
# from matplotlib import pyplot as plt
#
allHC = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature_246/allstruc/nocombat/allHC_GrayVol246_nocombat_final1030.csv')
                # 获取其他站点名称


tr = np.random.uniform(size=allHC.shape[0]) > 0.2  # 形成一个随机抽样
te = ~tr
allHC_tr = allHC.loc[tr]
allHC_te = allHC.loc[te]                            # 将fcon中数据一分为2 ture false
print(" -Data Done ! -")
#TODO:
processing_dir = "/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1030/NMResults/"
#
if not os.path.isdir(processing_dir):
    os.mkdir(processing_dir)
allHC_tr.to_csv(processing_dir + '/allHC_tr.csv')
allHC_te.to_csv(processing_dir + '/allHC_te.csv')

#
# #--要训练的脑区
brainRegion = allHC.columns.tolist()
idps = brainRegion[6:]

# print(len(idps))
os.chdir(processing_dir)
pro_dir = os.getcwd()
#  ---构建训练集---
X_train = (allHC_tr['age']/100).to_numpy(dtype=float)
Y_train = allHC_tr[idps].to_numpy(dtype=float)
batch_effects_train = allHC_tr[['sitenum','sex']].to_numpy(dtype=int)

with open('X_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_train), file)
with open('Y_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_train), file)
with open('trbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_train), file)

#  ---构建测试集---
X_test = (allHC_te['age']/100).to_numpy(dtype=float)
Y_test = allHC_te[idps].to_numpy(dtype=float)

batch_effects_test = allHC_te[['sitenum','sex']].to_numpy(dtype=int)
with open('X_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_test), file)
with open('Y_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_test), file)
with open('tsbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_test), file)


respfile = os.path.join(pro_dir, 'Y_train.pkl')       # measurements  (eg cortical thickness) of the training samples (columns: the various features/ROIs, rows: observations or subjects)
covfile = os.path.join(pro_dir, 'X_train.pkl')        # covariates (eg age) the training samples (columns: covariates, rows: observations or subjects)

testrespfile_path = os.path.join(pro_dir, 'Y_test.pkl')       # measurements  for the testing samples
testcovfile_path = os.path.join(pro_dir, 'X_test.pkl')        # covariate file for the testing samples

trbefile = os.path.join(pro_dir, 'trbefile.pkl')      # training batch effects file (eg scanner_id, gender)  (columns: the various batch effects, rows: observations or subjects)
tsbefile = os.path.join(pro_dir, 'tsbefile.pkl')      # testing batch effects file

output_path = os.path.join(pro_dir, 'Models/')    #  output path, where the models will be written

log_dir = os.path.join(pro_dir, 'log/')
if not os.path.isdir(output_path):
    os.mkdir(output_path)
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
outputsuffix = '_estimate'
ptk.normative.estimate(covfile=covfile,
                       respfile=respfile,
                       tsbefile=tsbefile,
                       trbefile=trbefile,
                       #inscaler='standardize',
                       #outscaler='standardize',
                       #linear_mu='True',
                       #random_intercept_mu='True',
                       #centered_intercept_mu='True',
                       alg='hbr',
                       log_path=log_dir,
                       binary=True,
                       output_path=output_path,
                       testcov= testcovfile_path,
                       testresp = testrespfile_path,
                       outputsuffix=outputsuffix,
                       savemodel=True)





#  ---构建MDD测试集---
allMDD = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature_246/allstruc/nocombat/'
                     'allMDDGrayVol246_sum_1030.csv')

X_mdd_test = (allMDD['age']/100).to_numpy(dtype=float)
Y_mdd_test = allMDD[idps].to_numpy(dtype=float)
print(X_mdd_test.shape)
print(Y_mdd_test.shape)

batch_effects_mdd_test = allMDD[['sitenum','sex']].to_numpy(dtype=int)
print('be---',batch_effects_mdd_test.shape)
with open('X_mdd_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_mdd_test), file)
with open('Y_mdd_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_mdd_test), file)
with open('tsbefile_mdd.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_mdd_test), file)

mddcovfile = os.path.join(pro_dir, 'X_mdd_test.pkl')
mddrespfile = os.path.join(pro_dir, 'Y_mdd_test.pkl')       # measurements  (eg cortical thickness) of the training samples (columns: the various features/ROIs, rows: observations or subjects)
mddtsbefile = os.path.join(pro_dir, 'tsbefile_mdd.pkl')      # testing batch effects file

#output_path = os.path.join(pro_dir, 'Models/')    #  output path, where the models will be written

log_dir = os.path.join(pro_dir, 'log/')
if not os.path.isdir(output_path):
    os.mkdir(output_path)
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
mddoutputsuffix = '_mdd'
yhat_te, s2_te, Z = ptk.normative.predict(
                            covfile=mddcovfile,
                            respfile=mddrespfile,
                            tsbefile=mddtsbefile,
                            alg='hbr',
                            log_path=log_dir,
                            binary=True,
                            model_path=output_path,
                            outputsuffix=mddoutputsuffix,
                            savemodel=True
)

