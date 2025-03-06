import pandas as pd

#alldata = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults/GrayVol246_Z_AllHCestimate.csv', index_col=0)
alldata = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1228/StaResults_test/GrayVol246_Z_AllMDD.csv', index_col=0)

data=alldata.iloc[:, 0:]
column_means = data.mean()


print(column_means)
df = pd.DataFrame(column_means)

#df.to_csv('./step4_AllHCestimate_Regionmean.csv')
df.to_csv('./step4_AllMDD_Regionmean.csv')