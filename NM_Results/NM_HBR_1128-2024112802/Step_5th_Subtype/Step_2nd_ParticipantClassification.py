import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import DBSCAN,AgglomerativeClustering
alldata = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol246_HBR_HCMDD_1129/StaResults/GrayVol246_Z_AllMDD.csv')

data = alldata.iloc[:,1:]



print(data)

data = np.array(data)
min_max_scaler = StandardScaler()
data = min_max_scaler.fit_transform(data)

kmeans = KMeans(n_clusters=2,init='k-means++',random_state=42)
kmeans.fit(data)

score = silhouette_score(data, kmeans.labels_)

print('silhouette_score--',score)

label_pred = kmeans.labels_
print(label_pred)
inertia = kmeans.inertia_
print('inertia--',inertia)

centroids = kmeans.cluster_centers_
# print('centroids--',centroids)
#
x0 = alldata[label_pred == 0]
x1 = alldata[label_pred == 1]
#x2 = alldata[label_pred == 2] # 分成3类，在此增加 x2 = data[label_pred == 2]

# group = pd.concat([x0,x1],axis=0)
# print(group)
df = pd.DataFrame(x0)
# print(df)
df.to_csv('./step2_group_subtype1.csv')

df1 = pd.DataFrame(x1)
df1.to_csv('./step2_group_subtype2.csv')

# df2 = pd.DataFrame(x2)
# df2.to_csv('./step2_group_subtype3.csv')

