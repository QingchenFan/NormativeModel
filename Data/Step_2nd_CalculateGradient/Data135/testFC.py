import glob

import seaborn as sns
import scipy.io as sio
from matplotlib import pyplot as plt
from nilearn import plotting
from nilearn import datasets



def hotmap(data,subid,path):
    cx = sns.heatmap(data,
                     xticklabels=False, yticklabels=False, cmap='Blues', annot=False,
                     #mask=mask
                    #cbar_kws ={'format': '%.1f','ticks': [-1.0, 0.0, 1.0]}
                    )    # xticklabels/yticklabels x轴的titel  "Spectral"
    cx.tick_params(labelsize=100, left=False, bottom=False)  # 控制去掉小刻度线


    cbar_3 = cx.collections[0].colorbar
    cbar_3.ax.tick_params(labelsize=12, left=False, right=False)
    plt.savefig(path + '/'+subid + '.png')
    plt.show()

path = '/Volumes/QCI/NormativeModel/Data135/HC/Data135_Schaefer400FC_mat/*/*.mat'
file = glob.glob(path)
for i in file:

    subid = i.split('/')[7]

    data = sio.loadmat(i)['data']
    pcnpath = '/Volumes/QCI/NormativeModel/Data135/HC/FC_PCN'
    hotmap(data,subid,pcnpath)