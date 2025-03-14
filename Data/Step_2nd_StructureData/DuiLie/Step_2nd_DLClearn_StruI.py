import glob
import pandas as pd

# --------shaefer 400 -----------
# datapath = glob.glob('/Volumes/QCI/NormativeModel/DuiLie/MDD/DuiLie_Strufeature/*')
# tmp = []
#
# for i in datapath:
#     print(i)
#     subID = i.split('/')[-1]
#     print(subID)
#
#     rhp = i + '/' + subID+'_rh.txt'
#     rh_data = pd.read_csv(rhp,skiprows = 61, delimiter = '\t',header=None)
#     rh_data.columns = ['Column1']
#     rh_data = rh_data['Column1'].str.split(n=9, expand=True)
#     rh_data.columns = ['StructName', 'NumVert', 'SurfArea' ,'GrayVol', 'ThickAvg', 'ThickStd', 'MeanCurv', 'GausCurv', 'FoldInd', 'CurvInd']
#     rh = rh_data[['StructName','GrayVol']].T   # TODO: ThickAvg / SurfArea / GrayVol
#
#     lhp = i + '/' + subID + '_lh.txt'
#     lh_data = pd.read_csv(lhp,skiprows = 61, delimiter = '\t',header=None)
#     lh_data.columns = ['Column1']
#     lh_data = lh_data['Column1'].str.split(n=9, expand=True)
#     lh_data.columns = ['StructName', 'NumVert', 'SurfArea' ,'GrayVol', 'ThickAvg', 'ThickStd', 'MeanCurv', 'GausCurv', 'FoldInd', 'CurvInd']
#     lh = lh_data[['StructName', 'GrayVol']].T  # TODO: ThickAvg / SurfArea / GrayVol
#
#     res = pd.concat([rh,lh],axis=1, ignore_index=True)
#     #print(res)
#     res.insert(0, 'subId', [' ', subID])
#     print(res)
#     res.to_csv(i +'/'+subID+'_GrayVol.csv',index=False)  # TODO: ThickAvg / SurfArea / GrayVol

# --------------brainnetome 246---------------------
datapath = glob.glob('/Volumes/QCI/NormativeModel/DuiLie/MDD/DuiLie_Strufeature_Brainnetom_V4/*')
tmp = []

for i in datapath:
    print(i)
    subID = i.split('/')[-1]
    print(subID)

    rhp = i + '/rh.BN_Atlas.txt'
    rh_data = pd.read_csv(rhp, skiprows=60, delimiter='\t', header=None)
    rh_data.columns = ['Column1']
    rh_data = rh_data['Column1'].str.split(n=9, expand=True)
    rh_data.columns = ['StructName', 'NumVert', 'SurfArea', 'GrayVol', 'ThickAvg', 'ThickStd', 'MeanCurv', 'GausCurv', 'FoldInd', 'CurvInd']
    rh = rh_data[['StructName', 'GrayVol']].T   # TODO: ThickAvg / SurfArea / GrayVol

    lhp = i + '/lh.BN_Atlas.txt'
    lh_data = pd.read_csv(lhp, skiprows=60, delimiter='\t', header=None)
    lh_data.columns = ['Column1']
    lh_data = lh_data['Column1'].str.split(n=9, expand=True)
    lh_data.columns = ['StructName', 'NumVert', 'SurfArea', 'GrayVol', 'ThickAvg', 'ThickStd', 'MeanCurv', 'GausCurv', 'FoldInd', 'CurvInd']
    lh = lh_data[['StructName', 'GrayVol']].T  # TODO: ThickAvg / SurfArea / GrayVol

    res = pd.concat([rh, lh], axis=1, ignore_index=True)
    #print(res)
    res.insert(0, 'subId', [' ', subID])
    print(res)
    res.to_csv(i +'/'+subID+'_GrayVol.csv', index=False)  # TODO: ThickAvg / SurfArea / GrayVol