#!/bin/bash
export FREESURFER_HOME=/Applications/freesurfer/7.4.1
export SUBJECTS_DIR=$FREESURFER_HOME/subjects
source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh

export SUBJECTS_DIR='/Volumes/QCII/Data135_processed/data135_HC_fmriprep_out/sourcedata/freesurfer'
newpath=/Volumes/QCI/NormativeModel/Data135/HC/Strufeature

mkdir $newpath

for subj in $(ls ${SUBJECTS_DIR} );
do
  if [ ! -d $newpath/${subj} ]; then
      mkdir $newpath/${subj}
  fi
  echo "${subj}";
  mri_surf2surf --hemi lh \
  --srcsubject fsaverage \
  --sval-annot /Users/qingchen/Documents/code/Data/annot/lh.Schaefer2018_400Parcels_17Networks_order.annot \
  --trgsubject ${subj} \
  --trgsurfval $newpath/${subj}/lh.Schaefer2018_400Parcels_17Networks_ind.annot

  mris_anatomical_stats -a $newpath/${subj}/lh.Schaefer2018_400Parcels_17Networks_ind.annot \
  -f  $newpath/${subj}/${subj}_lh.txt \
  -b ${subj} lh

done