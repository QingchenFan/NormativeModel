import os
import glob

path = '/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/sourcedata/freesurfer/*'
datapath = glob.glob(path)

for i in datapath:

    subID = i.split('/')[-1]
    print(subID)
    if 'fsaverage' in i:
        continue
    newpath = '/home/zhouyuan/fan/Data/brainproject_processed/HC_stru_brainnetom/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)

    inl = '''
            export SUBJECTS_DIR=''/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/sourcedata/freesurfer'';\
            mris_ca_label -l $SUBJECTS_DIR/'''+subID+'''/label/lh.cortex.label \
            '''+subID+''' \
            lh $SUBJECTS_DIR/'''+subID+'''/surf/lh.sphere.reg \
            /home/zhouyuan/fan/BrainnetomeAtlas/BN_Atlas_freesurfer/lh.BN_Atlas.gcs \
            '''+newpath+'''/lh.BN_Atlas.annot
        '''
    inr = '''
            export SUBJECTS_DIR=''/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/sourcedata/freesurfer'';\
            mris_ca_label -l $SUBJECTS_DIR/'''+subID+'''/label/rh.cortex.label \
            '''+subID+''' \
            rh $SUBJECTS_DIR/'''+subID+'''/surf/rh.sphere.reg \
            /home/zhouyuan/fan/BrainnetomeAtlas/BN_Atlas_freesurfer/rh.BN_Atlas.gcs \
            '''+newpath+'''/rh.BN_Atlas.annot
        '''
    incl = '''
            export SUBJECTS_DIR=''/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/sourcedata/freesurfer'';\
            mris_anatomical_stats -a '''+newpath+'''/lh.BN_Atlas.annot \
            -f '''+newpath+'''/lh.BN_Atlas.txt \
            -b '''+subID+''' lh 
        '''
    incr = '''
            export SUBJECTS_DIR=''/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/sourcedata/freesurfer'';\
            mris_anatomical_stats -a '''+newpath+'''/rh.BN_Atlas.annot \
            -f '''+newpath+'''/rh.BN_Atlas.txt \
            -b '''+subID+''' rh 
        '''

    os.system(inl)
    os.system(inr)
    os.system(incl)
    os.system(incr)
    exit()

