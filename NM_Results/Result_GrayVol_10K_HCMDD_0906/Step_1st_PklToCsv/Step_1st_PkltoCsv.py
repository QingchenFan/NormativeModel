import pandas as pd
import numpy as np

def pkltocsv(Resultpath,labelpath,columnsname,opath,mark):
    Rho_AllHCestimate = pd.read_pickle(Resultpath+'Rho_'+mark+'.pkl')

    pRho_AllHCestimate = pd.read_pickle(Resultpath+'pRho_'+mark+'.pkl')

    SMSE_AllHCestimate = pd.read_pickle(Resultpath+'SMSE_'+mark+'.pkl')

    RMSE_AllHCestimate = pd.read_pickle(Resultpath+'RMSE_'+mark+'.pkl')

    yhat_AllHCestimate = pd.read_pickle(Resultpath+'yhat_'+mark+'.pkl')


    label = pd.read_csv(labelpath)
    brainRegion = label.columns.tolist()
    del brainRegion[0:5]
    regions = pd.DataFrame(brainRegion)
    m = []
    for num,re in enumerate(brainRegion):
        a = yhat_AllHCestimate[num]
        b = label[re]
        MAE = np.mean(np.abs(a - b))
        m.append(MAE)
    mae = pd.DataFrame(m)

    df_sum = pd.concat([regions, Rho_AllHCestimate, pRho_AllHCestimate, RMSE_AllHCestimate, SMSE_AllHCestimate, mae],
                       axis=1)  # 将两列拼接在一起，axis=1 表示按列拼接
    df_sum.columns = columnsname
    df_sum.to_csv(opath)

Resultpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10k_HCMDD_0906/NMResults/'
labelpath = '/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstrucIII/combat/allHC_GrayVol_combat_final_0906.csv'
columnsname = ['Regions','Rho_estimate', 'pRho_estimate', 'RMSE_estimate', 'SMSE_estimate', 'MAE']
opath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0906/StaResults/GrayVol_ResSum.csv'
mark = 'AllHCestimate'
pkltocsv(Resultpath,labelpath,columnsname,opath,mark)

Resultpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10k_HCMDD_0906/NMResults/'
mddlabel = '/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstrucIII/combat/allMDD_GrayVol_combat_final_0906.csv'
opath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10K_HCMDD_0906/StaResults/GrayVol_MDD_ResSum.csv'
mark = 'AllHCMDD'
pkltocsv(Resultpath,mddlabel,columnsname,opath,mark)