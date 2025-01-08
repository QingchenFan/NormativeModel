import numpy as np
import pandas as pd
from scipy.io import savemat
data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/subtype2_ZvalueHAMD.csv')
data = np.array(data)
savemat('./subtype2_ZvalueHAMD.mat', {'s2': data})
