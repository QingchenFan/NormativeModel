import os
import glob

path = '/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out/fmriprep/*/sourcedata/freesurfer'
datapath = glob.glob(path)
for i in datapath:
    subID = i.split('/')[-3]
    print(subID)
    newpath = '/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature_Brainnetom/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)

    inl = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR='/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out/fmriprep/'''+subID+'''/sourcedata/freesurfer';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_ca_label -l $SUBJECTS_DIR/'''+subID+'''/label/lh.cortex.label \
            '''+subID+''' \
            lh $SUBJECTS_DIR/'''+subID+'''/surf/lh.sphere.reg \
            /Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/lh.BN_Atlas.gcs \
            '''+newpath+'''/lh.BN_Atlas.annot
        '''
    inr = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR='/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out/fmriprep/'''+subID+'''/sourcedata/freesurfer';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_ca_label -l $SUBJECTS_DIR/'''+subID+'''/label/rh.cortex.label \
            '''+subID+''' \
            rh $SUBJECTS_DIR/'''+subID+'''/surf/rh.sphere.reg \
            /Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/rh.BN_Atlas.gcs \
            '''+newpath+'''/rh.BN_Atlas.annot
        '''
    incl = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR='/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out/fmriprep/'''+subID+'''/sourcedata/freesurfer';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_anatomical_stats -a '''+newpath+'''/lh.BN_Atlas.annot \
            -f '''+newpath+'''/lh.BN_Atlas.txt \
            -b '''+subID+''' lh 
        '''
    incr = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR='/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out/fmriprep/'''+subID+'''/sourcedata/freesurfer';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_anatomical_stats -a '''+newpath+'''/rh.BN_Atlas.annot \
            -f '''+newpath+'''/rh.BN_Atlas.txt \
            -b '''+subID+''' rh 
        '''

    os.system(inl)
    os.system(inr)
    os.system(incl)
    os.system(incr)

