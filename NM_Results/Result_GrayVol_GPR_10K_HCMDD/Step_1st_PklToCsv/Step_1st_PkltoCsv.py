import pandas as pd
import numpy as np

def pkltocsv(Resultpath,labelpath,columnsname,opath,mark):
    Rho_AllHCestimate = pd.read_pickle(Resultpath+'Rho_'+mark+'.pkl')
    print(Rho_AllHCestimate.shape)
    pRho_AllHCestimate = pd.read_pickle(Resultpath+'pRho_'+mark+'.pkl')
    print(pRho_AllHCestimate.shape)
    SMSE_AllHCestimate = pd.read_pickle(Resultpath+'SMSE_'+mark+'.pkl')
    print(SMSE_AllHCestimate.shape)
    RMSE_AllHCestimate = pd.read_pickle(Resultpath+'RMSE_'+mark+'.pkl')
    print(RMSE_AllHCestimate.shape)
    yhat_AllHCestimate = pd.read_pickle(Resultpath+'yhat_'+mark+'.pkl')
    print(yhat_AllHCestimate.shape)
    EXPV_AllHCestimate = pd.read_pickle(Resultpath + 'EXPV_' + mark + '.pkl')
    print(EXPV_AllHCestimate.shape)
    MSLL_AllHCestimate = pd.read_pickle(Resultpath + 'MSLL_' + mark + '.pkl')

    label = pd.read_csv(labelpath)
    brainRegion = label.columns.tolist()
    a = brainRegion[7:]
    regions = pd.DataFrame(a)

    # m = []
    # for num,re in enumerate(brainRegion):
    #     a = yhat_AllHCestimate[num]
    #     b = label[re]
    #     print('a-',a)
    #     print('b-',b)
    #     MAE = np.mean(np.abs(a - b))
    #     m.append(MAE)
    # mae = pd.DataFrame(m)

    df_sum = pd.concat([regions, Rho_AllHCestimate, pRho_AllHCestimate, RMSE_AllHCestimate, SMSE_AllHCestimate, EXPV_AllHCestimate,MSLL_AllHCestimate],
                       axis=1)  # 将两列拼接在一起，axis=1 表示按列拼接
    df_sum.columns = columnsname
    df_sum.to_csv(opath)
columnsname = ['Regions','Rho_estimate', 'pRho_estimate', 'RMSE_estimate', 'SMSE_estimate', 'EXPV','MSLL']

Resultpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_10K_HCMDD_1022/NMResults/'
labelpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_10K_HCMDD_1022/NMResults/allHC_GrayVol246_combat_final.csv'
opath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_10K_HCMDD_1022/StaResults/GPR_GrayVol246_HC_ResSum.csv'
mark = 'AllHCestimate'
pkltocsv(Resultpath,labelpath,columnsname,opath,mark)
#
# Resultpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_10K_HCMDD_1022/NMResults/'
# mddlabel = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_10K_HCMDD_1022/NMResults/allMDD_GrayVol246_combat_final.csv'
# opath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_GPH_10K_HCMDD_1022/StaResults/GPR_GrayVol246_MDD_ResSum.csv'
# mark = 'AllMDD'
# pkltocsv(Resultpath,mddlabel,columnsname,opath,mark)