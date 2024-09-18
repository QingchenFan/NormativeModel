import glob
import scipy.io as sio
import pandas as pd
path = '/Users/qingchen/Documents/Data/HCP/HCPData/HCPGradient/*'
file = glob.glob(path)
box = []
idbox = []
for i in file:
    m = sio.loadmat(i)['data']
    FG = m[:,0:1].T[0]
    box.append(FG)
    idbox.append(i[-23:-13])

df = pd.DataFrame(box)
df.index = idbox

label = pd.read_csv('./atlas-Schaefer2018v0143_desc-400ParcelsAllNetworks_dseg.csv')
print(label)

df.columns = label['label'].tolist()

df.to_csv('./feature_HC.csv')
