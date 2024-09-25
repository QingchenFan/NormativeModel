
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

data = pd.read_csv('/Volumes/QCI/NormativeModel/Results/Result_GrayVol_10k_HCMDD_0906/StaResults/GrayVol_Z_AllHCMDD.csv')
data = data.iloc[:,1:]


data = np.array(data)
min_max_scaler = MinMaxScaler()
data = min_max_scaler.fit_transform(data)

all_mean = []
silhouette_s = []
for k in np.arange(2,11):
    for i in np.arange(1,101):
        print('-k-',k)
        kmeans = KMeans(n_clusters=k,init='k-means++',random_state=6)

        kmeans.fit(data)
        score = silhouette_score(data, kmeans.labels_)
        silhouette_s.append(score)

        label_pred = kmeans.labels_

        inertia = kmeans.inertia_


    mean_score = np.mean(np.array(silhouette_s))
    print(mean_score)
    all_mean.append(mean_score)
print(all_mean)
df = pd.DataFrame(all_mean)
df.to_csv('./Step1_1_silhouette_score.csv')