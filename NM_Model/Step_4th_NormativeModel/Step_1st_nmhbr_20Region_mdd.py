import glob
import os
from shutil import copy

import pandas as pd
import pcntoolkit as ptk
import numpy as np
import pickle
from matplotlib import pyplot as plt
transferModelPath = '/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/Result/Transfer/'
files = glob.glob(os.path.join(transferModelPath, '*'))
pkl_files = sorted(files, key=lambda x: int(os.path.basename(x).split('_')[-2]))
metadata = '/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/Result/Transfer/'

#--要训练的脑区
idps = ['LH_Vis_1','LH_Default_PFC_12','LH_DorsAttn_PrCv_1','LH_Default_pCunPCC_5','LH_SalVentAttn_TempOcc_1',
        'LH_Limbic_OFC_1','LH_Limbic_TempPole_5','LH_Cont_Par_3','LH_Cont_pCun_2','LH_Default_Temp_6',
        'RH_Vis_8','RH_Vis_18','RH_SomMot_3','RH_SomMot_15','RH_SomMot_30','RH_DorsAttn_Post_2',
        'RH_DorsAttn_Post_12','RH_SalVentAttn_Med_5','RH_Limbic_OFC_3','RH_Cont_Par_1'
        ]
for idp_num ,idp in enumerate(idps):
    pro_dir = '/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/Result_MDD_'+ str(idp_num) +'/'
    if not os.path.isdir(pro_dir):
        os.mkdir(pro_dir)
    os.chdir(pro_dir)
    pro_dir = os.getcwd()

    newModel = pro_dir + '/Model_' + str(idp_num) + '/'
    if not os.path.exists(newModel):
        os.mkdir(newModel)
    copy(pkl_files[idp_num],newModel)


    # -- 构建 MDD x y
    anding_mdd = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/andingMddGradientfeature.csv')
    anding_mdd_X_test = (anding_mdd['age'] / 100).to_numpy(dtype=float)
    anding_mdd_Y_test = anding_mdd[idp].to_numpy(dtype=float)

    anding_mdd_batch_effects_test = anding_mdd[['sitenum']].to_numpy(dtype=int)

    with open('anding_mdd_X_test.pkl', 'wb') as file:
        pickle.dump(pd.DataFrame(anding_mdd_X_test), file)
    with open('anding_mdd_Y_test.pkl', 'wb') as file:
        pickle.dump(pd.DataFrame(anding_mdd_Y_test), file)
    with open('anding_mdd_tsbefile.pkl', 'wb') as file:
        pickle.dump(pd.DataFrame(anding_mdd_batch_effects_test), file)
    testcov = os.path.join(pro_dir,'anding_mdd_X_test.pkl')  # training batch effects file (eg scanner_id, gender)  (columns: the various batch effects, rows: observations or subjects)
    testresp = os.path.join(pro_dir, 'anding_mdd_Y_test.pkl')
    tsbefile = os.path.join(pro_dir, 'anding_mdd_tsbefile.pkl')


    log_dir = os.path.join(pro_dir, 'log_transfer/')
    output_path = os.path.join(pro_dir, 'Transfer_MDD_'+str(idp_num) + '/')
    model_path = os.path.join(pro_dir, 'Model_' + str(idp_num) + '/')  # path to the previously trained models
    print(model_path)
    print('Transfer_MDD_'+str(idp_num) + '/')
    with open('/Users/qingchen/Documents/code/NormativeModelMDD/Step_4th_NormativeModel/Data/Result_MDD_0/Model_0/NM_0_0_transfer.pkl', 'rb') as file:
        data = pickle.load(file)
        print(data)

    outputsuffix = '_MDD'
    # --最终训练模型
    yhat, s2, z_scores = ptk.normative.predict( covfile=testcov,
                                                respfile=testresp,
                                                tsbefile=tsbefile,
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
                                                outputsuffix=outputsuffix,
                                                inputsuffix='transfer',
                                                savemodel=True)
    print(yhat)