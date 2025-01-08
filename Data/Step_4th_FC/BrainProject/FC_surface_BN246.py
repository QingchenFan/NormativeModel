import glob
import os
import numpy as np
import nibabel as nib
from nilearn.maskers import NiftiMasker
from scipy.io import savemat
from nilearn import plotting
def volume_from_cifti(data, axis):
    assert isinstance(axis, nib.cifti2.BrainModelAxis)
    data = data.T[axis.volume_mask]                          # Assume brainmodels axis is last, move it to front
    volmask = axis.volume_mask                               # Which indices on this axis are for voxels?
    vox_indices = tuple(axis.voxel[axis.volume_mask].T)      # ([x0, x1, ...], [y0, ...], [z0, ...])
    vol_data = np.zeros(axis.volume_shape + data.shape[1:],  # Volume + any extra dimensions
                        dtype=data.dtype)
    vol_data[vox_indices] = data                             # "Fancy indexing"
    return nib.Nifti1Image(vol_data, axis.affine)

def surf_data_from_cifti(data, axis, surf_name):
    assert isinstance(axis, nib.cifti2.BrainModelAxis)
    for name, data_indices, model in axis.iter_structures():  # Iterates over volumetric and surface structures
        if name == surf_name:                                 # Just looking for a surface
            data = data.T[data_indices]                       # Assume brainmodels axis is last, move it to front
            vtx_indices = model.vertex                        # Generally 1-N, except medial wall vertices
            surf_data = np.zeros((vtx_indices.max() + 1,) + data.shape[1:], dtype=data.dtype)
            surf_data[vtx_indices] = data
            return surf_data
    raise ValueError(f"No structure named {surf_name}")

def loadData(datapath):
    cifti = nib.load(datapath)
    cifti_data = cifti.get_fdata()
    cifti_hdr = cifti.header
    axes = [cifti_hdr.get_axis(i) for i in range(cifti.ndim)]
    return cifti, cifti_data, cifti_hdr, axes

def plot_correlation_matrix(correlation_matrix, labels):
    plotting.plot_matrix(
        correlation_matrix,
        figure=(10, 8),
        labels=labels,
        vmax=0.8,
        vmin=-0.8,
        #title="Confounds",
        reorder=True,
    )
    plotting.show()
def subc_timeseries(data,atlaspath):
    data = data.transpose(3, 0, 1, 2)
    atlasData = nib.load(atlaspath).get_fdata()

    atlasData = np.reshape(atlasData, (1, 91 * 109 * 91), order='F')

    data = np.reshape(data, (data.shape[0], 91 * 109 * 91), order='F')

    roilist = []
    for r in range(211, 247):

        index = np.where(atlasData == r)

        roi = data[:, index[1]]  # 将第r个脑区中的voxel 数据（时间序列）提取

        # 统计体素个数
        totalvoxel = roi.shape[1] if roi.shape[1] > 0 else 1

        sum = np.sum(roi, axis=1)

        roiBoldsum = sum / totalvoxel

        roilist.append(roiBoldsum)

    subctimeseries = np.array(roilist)
    print('subctimeseries.shape-', subctimeseries.shape)
    subcFC = np.corrcoef(subctimeseries)
    return subcFC, subctimeseries




def calculate_FC(dpath,tpath,atlaspath,regions):
    #datapath = '/Users/qingchen/Documents/code/Data/FC/sub-06202_task-rest_space-fsLR_den-91k_desc-denoisedSmoothed_bold.dtseries.nii'
    datapath = dpath
    cifti, cifti_data, cifti_hdr, axes = loadData(datapath)
    axes = [cifti_hdr.get_axis(i) for i in range(cifti.ndim)]

    Subcortical_Data = volume_from_cifti(cifti_data, axes[1])
    Subcortical_Data = Subcortical_Data.get_fdata()

    _, subctimeseries = subc_timeseries(Subcortical_Data, atlaspath)
    # savemat('./subcFC.mat', {'data': subcFC})
    # savemat('./subctimeseries.mat', {'data': subctimeseries})

    a_left = surf_data_from_cifti(cifti_data, axes[1], 'CIFTI_STRUCTURE_CORTEX_LEFT')
    a_right = surf_data_from_cifti(cifti_data, axes[1], 'CIFTI_STRUCTURE_CORTEX_RIGHT')
    cortex_data = np.concatenate((a_left, a_right), axis=0)
    #print('cortex_data',cortex_data.shape)
    template = tpath
    label = nib.load(template).get_fdata()
    label[label > 210] -= 210

    if label.shape[1] == 59412:
        cortex_data = nib.load(datapath).get_fdata()[:, 0:59412].T
    roilist = []
    for i in range(1, regions + 1):
        index = np.where(label == i)
        roi = cortex_data[index[1], :]
        roilist.append(np.mean(roi, axis=0))

    roiMatrix = np.array(roilist)
    vertexsubc = np.vstack((roiMatrix, subctimeseries))
    resFC = np.corrcoef(vertexsubc)
    print('FC shape : ', resFC.shape)
    return resFC


datapath = '/Volumes/QCI/NormativeModel/BrainProject/MDDdtseriesnii/*/*ap*'
tpath = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/fsaverage/fsaverage_LR32k/fsaverage.BN_Atlas.32k_fs_LR.dlabel.nii'
atlaspath = '/Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_246_2mm.nii.gz'
data = glob.glob(datapath)
for i in data:
    subID = i.split('/')[-2]
    print(subID)

    resFC = calculate_FC(i, tpath, atlaspath, 210)
    outpath = '/Volumes/QCI/NormativeModel/BrainProject/MDD_BN246FC/' + subID +'_FC.mat'
    savemat(outpath, {'data': resFC})

