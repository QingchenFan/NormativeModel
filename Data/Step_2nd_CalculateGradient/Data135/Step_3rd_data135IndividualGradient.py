import glob
import numpy as np
import scipy.io as scio
from brainspace.datasets import load_parcellation, load_conte69
from brainspace.gradient import GradientMaps
from brainspace.plotting import plot_hemispheres
from brainspace.utils.parcellation import map_to_labels
from scipy.io import savemat

path = '/Volumes/QCI/NormativeModel/Data135/HC/Data135_Schaefer400FC_mat/*/sub*'

dataList = glob.glob(path)
databox = []
ref = scio.loadmat('/Volumes/QCI/NormativeModel/Data135/HC/Data135_HC_GroupGradient.mat')

for i in dataList:
    data = scio.loadmat(i)['data']
    print(i)
    subId = i.split('/')[7]

    gp = GradientMaps(kernel='normalized_angle', approach='dm', alignment='procrustes', n_components=10,
                      random_state=0)
    gp.fit(data,reference=ref['data'])
    res = gp.gradients_

    savemat('/Volumes/QCI/NormativeModel/Data135/MDD/Data135_IndividualGradient/'+subId+'_gradient.mat',{'data':res})

    # Plot brain gradient
    labeling = load_parcellation('schaefer', scale=400, join=True)
    surf_lh, surf_rh = load_conte69()
    mask = labeling != 0

    grad = [None] * 2

    for i in range(2):
        # map the gradient to the parcels
        grad[i] = map_to_labels(res[:, i], labeling, mask=mask, fill=np.nan)
    picname = '/Volumes/QCI/NormativeModel/Data135/MDD/Data135_Gradientplot/'+subId+'.png'
    plot_hemispheres(surf_lh, surf_rh,screenshot=True,filename=picname, array_name=grad, size=(2000, 800), cmap='coolwarm',
                     color_bar=True, label_text=['Grad1', 'Grad2'], zoom=1)
