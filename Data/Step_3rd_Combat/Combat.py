from neuroCombat import neuroCombat
import pandas as pd
import numpy as np

# Getting example data
alldata = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/StructureFeature/allstrucII/nocombat/allsubGrayVol.csv')
#alldata = pd.read_csv('/Volumes/QCI/NormativeModel/FeatureData/allSubGradientfeature.csv')
data = alldata.iloc[:,5:]
data = np.array(data).T

#a = np.where(np.isinf(data))  # 判断异常值

covars = alldata[['sitenum','sex','age']]

covars.columns=['batch','gender','age']


# To specify names of the variables that are categorical:
categorical_cols = ['gender']
continuous_cols=['age']
# To specify the name of the variable that encodes for the scanner/batch covariate:
batch_col = 'batch'

#Harmonization step:
data_combat = neuroCombat(dat=data,
    covars=covars,  
    batch_col=batch_col,
    categorical_cols=categorical_cols,
    continuous_cols=continuous_cols)["data"]

data_combat = data_combat.T
print(data_combat)
np.savetxt('./allSub_GrayVol_combat.csv', data_combat, delimiter=',')
