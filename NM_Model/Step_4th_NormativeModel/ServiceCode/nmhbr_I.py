import os
import pandas as pd
import pcntoolkit as ptk
import numpy as np
import pickle
from matplotlib import pyplot as plt

allHC = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/allHCfeature.csv')
anding = allHC.loc[allHC['site'] == 'anding']                                   # 获取site = "anding"
anding['sitenum'] = 0                                                           # 加一列，标识站点 - 0

allHC = allHC.loc[allHC['site'] != 'anding']                                    # 获取其他站点的数据(此时的allHC,从allHC中排除了anding 站点
sites = allHC['site'].unique()                                                  # 获取其他站点名称

allHC['sitenum'] = 0

#-- train data \ test data
tr = np.random.uniform(size=allHC.shape[0]) > 0.5                                # 形成一个随机抽样(将AllHC的数据分为训练集和测试集
te = ~tr
allHC_tr = allHC.loc[tr]
allHC_te = allHC.loc[te]                                                         # 将AllHC中数据一分为2 ture false

#-- AllHC 分成训练集、测试集并保存到CSV文件中，anding同样操作
processing_dir = "/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data"
if not os.path.isdir(processing_dir):
    os.mkdir(processing_dir)
allHC_tr.to_csv(processing_dir + '/allHC_tr.csv')
allHC_te.to_csv(processing_dir + '/allHC_te.csv')


#--要训练的脑区
brainRegion = allHC.columns.tolist()
del brainRegion[0:4]
del brainRegion[-1:]

idps = brainRegion
# idps = ['LH_Vis_21','LH_Vis_22','LH_Vis_23','LH_Vis_24','LH_Vis_25','LH_Vis_26',
#         'LH_Vis_27','LH_Vis_28','LH_Vis_29','LH_Vis_30']
#--构建模型的x、y

pro_dir = '/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/Result'
if not os.path.isdir(pro_dir):
    os.mkdir(pro_dir)
os.chdir(pro_dir)
pro_dir = os.getcwd()

X_train = (allHC_tr['age']/100).to_numpy(dtype=float)
#print(X_train)
Y_train = allHC_tr[idps].to_numpy(dtype=float)
#print(Y_train)
batch_effects_train = allHC_tr[['sitenum']].to_numpy(dtype=int)

with open('X_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_train), file)
with open('Y_train.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_train), file)
with open('trbefile.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_train), file)


X_test = (allHC_te['age']/100).to_numpy(dtype=float)
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
#--生成对应路径，方便传入参数
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
#--训练模型
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