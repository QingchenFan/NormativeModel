import os
import pandas as pd
import pcntoolkit as ptk
import numpy as np
import pickle
import sys

print(sys.version)
#
# # a simple function to quickly load pickle files
def ldpkl(filename: str):
    with open(filename, 'rb') as f:
        return pickle.load(f)
# from matplotlib import pyplot as plt
#
allHC = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/Feature/'
                    'allHC_GrayVol246_nocombat_final1129.csv')
                # 获取其他站点名称

#TODO:
processing_dir = "/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/"
#
if not os.path.isdir(processing_dir):
    os.mkdir(processing_dir)

#
# #--要训练的脑区
brainRegion = allHC.columns.tolist()
idps = brainRegion[6:]

print(idps)

os.chdir(processing_dir)
pro_dir = os.getcwd()

output_path = os.path.join(pro_dir, 'Models/')



#  ---构建MDD测试集---
allMDD = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/Feature/'
                     'PDND_GrayVol_BN224_52w.csv')

X_mdd_test = (allMDD['age']/100).to_numpy(dtype=float)
Y_mdd_test = allMDD[idps].to_numpy(dtype=float)
print(X_mdd_test.shape)
print(Y_mdd_test.shape)

batch_effects_mdd_test = allMDD[['sitenum', 'sex']].to_numpy(dtype=int)
print('be---', batch_effects_mdd_test.shape)
with open('X52_mdd_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(X_mdd_test), file)
with open('Y52_mdd_test.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(Y_mdd_test), file)
with open('tsbefile52_mdd.pkl', 'wb') as file:
    pickle.dump(pd.DataFrame(batch_effects_mdd_test), file)

mddcovfile = os.path.join(pro_dir, 'X52_mdd_test.pkl')
mddrespfile = os.path.join(pro_dir, 'Y52_mdd_test.pkl')       # measurements  (eg cortical thickness) of the training samples (columns: the various features/ROIs, rows: observations or subjects)
mddtsbefile = os.path.join(pro_dir, 'tsbefile52_mdd.pkl')      # testing batch effects file

#output_path = os.path.join(pro_dir, 'Models/')    #  output path, where the models will be written

log_dir = os.path.join(pro_dir, 'log/')
if not os.path.isdir(output_path):
    os.mkdir(output_path)
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
mddoutputsuffix = '52_mdd'

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

