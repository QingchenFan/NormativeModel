import pandas as pd
import numpy as np

def pkltocsv(Resultpath,labelpath,columnsname,opath,mark):
    Rho_AllHCestimate = pd.read_pickle(Resultpath+'Rho_'+mark+'.pkl')
    print('r - ',Rho_AllHCestimate)
    pRho_AllHCestimate = pd.read_pickle(Resultpath+'pRho_'+mark+'.pkl')

    SMSE_AllHCestimate = pd.read_pickle(Resultpath+'SMSE_'+mark+'.pkl')

    RMSE_AllHCestimate = pd.read_pickle(Resultpath+'RMSE_'+mark+'.pkl')

    yhat_AllHCestimate = pd.read_pickle(Resultpath+'yhat_'+mark+'.pkl')
    print('yhat- ',yhat_AllHCestimate.shape)
    EXPV_AllHCestimate = pd.read_pickle(Resultpath + 'EXPV_' + mark + '.pkl')
    print('EXPV - ',EXPV_AllHCestimate.shape)
    MSLL_AllHCestimate = pd.read_pickle(Resultpath + 'MSLL_' + mark + '.pkl')

    label = pd.read_csv(labelpath)
    brainRegion = label.columns.tolist()
    a = brainRegion[7:]
    regions = pd.DataFrame(a)
    print(regions)
    print(len(regions))
    # m = []
    # for num,re in enumerate(brainRegion):
    #     a = yhat_AllHCestimate[num]
    #     b = label[re]
    #     MAE = np.mean(np.abs(a - b))
    #     m.append(MAE)
    # mae = pd.DataFrame(m)

    df_sum = pd.concat([regions, Rho_AllHCestimate, pRho_AllHCestimate, RMSE_AllHCestimate, SMSE_AllHCestimate, EXPV_AllHCestimate,MSLL_AllHCestimate],
                       axis=1)  # 将两列拼接在一起，axis=1 表示按列拼接
    df_sum.columns = columnsname
    df_sum.to_csv(opath)
columnsname = ['Regions','Rho_estimate', 'pRho_estimate', 'RMSE_estimate', 'SMSE', 'EXPV','MSLL']

Resultpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/'
labelpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/NMResults/allHC_te.csv'
opath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/hbr_estimate_GrayVol246_ResSum.csv'
mark = 'estimate'
pkltocsv(Resultpath, labelpath, columnsname, opath, mark)
#
# Resultpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1018/NMResults/'
# mddlabel = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1018/NMResults/allHC_anding_te.csv'
# opath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1018/StaResults/hbr_transfer_GrayVol246_ResSum.csv'
# mark = 'transfer'
# pkltocsv(Resultpath,mddlabel,columnsname,opath,mark)
#
# Resultpath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1028/NMResults/'
# mddlabel = '/Volumes/QCI/NormativeModel/FeatureData/StructureFeature_246/allstruc/nocombat/allMDDGrayVol246_sum.csv'
# opath = '/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1028/StaResults/hbr_mdd_GrayVol246_ResSum.csv'
# mark = 'mdd'
# pkltocsv(Resultpath,mddlabel,columnsname,opath,mark)