import os
import pandas as pd
import pcntoolkit as ptk
import numpy as np
import pickle
from matplotlib import pyplot as plt

allHC = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/allHCfeature.csv')
anding = allHC.loc[allHC['site'] == 'anding']                                   # 获取site = "anding"
anding['sitenum'] = 0                                                           # 加一列，标识站点 - 0

                                                  # 获取其他站点名称
tr = np.random.uniform(size=anding.shape[0]) > 0.5                               # 将anding 数据也形成一个随机抽样,形成训练集、测试集
te = ~tr

anding_tr = anding.loc[tr]                                                       # 训练集
anding_te = anding.loc[te]                                                       # 测试集


#-- AllHC 分成训练集、测试集并保存到CSV文件中，anding同样操作
processing_dir = "/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data"
if not os.path.isdir(processing_dir):
    os.mkdir(processing_dir)

anding_tr.to_csv(processing_dir + '/allHC_anding_tr.csv')
anding_te.to_csv(processing_dir + '/allHC_anding_te.csv')
#--要训练的脑区
brainRegion = allHC.columns.tolist()
del brainRegion[0:4]
del brainRegion[-1:]
idps = brainRegion
pro_dir = '/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/Result'
if not os.path.isdir(pro_dir):
    os.mkdir(pro_dir)
os.chdir(pro_dir)
pro_dir = os.getcwd()
#----------------------------微调模型------------------------------------
# --构建模型的x、y
X_adapt = (anding_tr['age']/100).to_numpy(dtype=float)
Y_adapt = anding_tr[idps].to_numpy(dtype=float)
#batch_effects_adapt = icbm_tr[['sitenum','sex']].to_numpy(dtype=int)
batch_effects_adapt = anding_tr[['sitenum']].to_numpy(dtype=int)

with open('X_adaptation.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_adapt), file)
with open('Y_adaptation.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_adapt), file)
with open('adbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_adapt), file)

# Test data (new dataset)
X_test_txfr = (anding_te['age']/100).to_numpy(dtype=float)
Y_test_txfr = anding_te[idps].to_numpy(dtype=float)
batch_effects_test_txfr = anding_te[['sitenum']].to_numpy(dtype=int)

with open('X_test_txfr.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_test_txfr), file)
with open('Y_test_txfr.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_test_txfr), file)
with open('txbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_test_txfr), file)

respfile = os.path.join(pro_dir, 'Y_adaptation.pkl')
covfile = os.path.join(pro_dir, 'X_adaptation.pkl')
testrespfile_path = os.path.join(pro_dir, 'Y_test_txfr.pkl')
testcovfile_path = os.path.join(pro_dir, 'X_test_txfr.pkl')
trbefile = os.path.join(pro_dir, 'adbefile.pkl')
tsbefile = os.path.join(pro_dir, 'txbefile.pkl')

log_dir = os.path.join(pro_dir, 'log_transfer/')
output_path = os.path.join(pro_dir, 'Transfer/')
model_path = os.path.join(pro_dir, 'Models/')  # path to the previously trained models
print(model_path)
outputsuffix = '_transfer'
#--最终训练模型
yhat, s2, z_scores = ptk.normative.transfer(covfile=covfile,
                                            respfile=respfile,
                                            tsbefile=tsbefile,
                                            trbefile=trbefile,
                                            #inscaler='standardize',
                                            #outscaler='standardize',
                                            #linear_mu='True',
                                            #random_intercept_mu='True',
                                            #centered_intercept_mu='True',
                                            model_path = model_path,
                                            alg='hbr',
                                            log_path=log_dir,
                                            binary=True,
                                            output_path=output_path,
                                            testcov= testcovfile_path,
                                            testresp = testrespfile_path,
                                            outputsuffix=outputsuffix,
                                            savemodel=True)
