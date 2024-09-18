import glob
import numpy as np
import scipy.io as scio
from brainspace.datasets import load_parcellation, load_conte69
from brainspace.gradient import GradientMaps
from brainspace.plotting import plot_hemispheres
from brainspace.utils.parcellation import map_to_labels
from scipy.io import savemat

path = '/Volumes/QCI/NormativeModel/DuiLie/HC/DuiLie_Schaefer400FC_mat/*/sub*'

dataList = glob.glob(path)
databox = []
box = np.zeros([400,400])
for i in dataList:
    print(i)
    data = scio.loadmat(i)['data']
    fizFC = np.arctanh(data)
    box = np.add(box,fizFC)

mfizFC = box / len(dataList)
mFC = np.tanh(mfizFC)
savemat('mFC.mat', {'mFC':mFC})
gp = GradientMaps(kernel='normalized_angle', approach='dm', alignment='procrustes', n_components=10,
                  random_state=0)

ref = scio.loadmat('/Users/qingchen/Documents/code/NormativeModelMDD/Step_2nd_CalculateGradient/HCP/GroupGradient.mat')
gp.fit(mFC,reference=ref['data'])
#gp.fit(mFC)
res = gp.gradients_

savemat('Duilie_HC_GroupGradient.mat', {'data':res})

# Plot brain gradient
labeling = load_parcellation('schaefer', scale=400, join=True)
surf_lh, surf_rh = load_conte69()
mask = labeling != 0

grad = [None] * 2

for i in range(2):
    # map the gradient to the parcels
    grad[i] = map_to_labels(res[:, i], labeling, mask=mask, fill=np.nan)

plot_hemispheres(surf_lh, surf_rh, array_name=grad, size=(2000, 800), cmap='coolwarm',
                 color_bar=True, label_text=['Grad1', 'Grad2'], zoom=1)
