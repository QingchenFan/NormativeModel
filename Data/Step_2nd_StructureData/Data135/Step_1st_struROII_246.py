import os
import glob
'''
    因为 fmriprep 运行环境不同，导致输出的 freesurfer结果目录不同，所以写了两个代码来处理
'''

path = '/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out_V2/sourcedata/freesurfer/*'
datapath = glob.glob(path)

for i in datapath:

    subID = i.split('/')[-1]
    print(subID)

    if 'fsaverage' in i:
        continue
    # expath = '/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature_BrainnetomV2/'+ subID
    # if os.path.exists(expath):
    #     continue
    newpath = '/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature_BrainnetomV2/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)

    inl = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out_V2/sourcedata/freesurfer/'';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_ca_label -l $SUBJECTS_DIR/'''+subID+'''/label/lh.cortex.label \
            '''+subID+''' \
            lh $SUBJECTS_DIR/'''+subID+'''/surf/lh.sphere.reg \
            /Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/lh.BN_Atlas.gcs \
            '''+newpath+'''/lh.BN_Atlas.annot
        '''
    inr = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out_V2/sourcedata/freesurfer'';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_ca_label -l $SUBJECTS_DIR/'''+subID+'''/label/rh.cortex.label \
            '''+subID+''' \
            rh $SUBJECTS_DIR/'''+subID+'''/surf/rh.sphere.reg \
            /Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/rh.BN_Atlas.gcs \
            '''+newpath+'''/rh.BN_Atlas.annot
        '''
    subint = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out_V2/sourcedata/freesurfer'';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mri_ca_label $SUBJECTS_DIR/'''+subID+'''/mri/brain.mgz  \
            $SUBJECTS_DIR/'''+subID+'''/mri/transforms/talairach.m3z \
            /Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/BN_Atlas_subcortex.gca \
            '''+newpath+'''/BN_Atlas_subcotex.mgz
            '''
    incl = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out_V2/sourcedata/freesurfer'';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_anatomical_stats -a '''+newpath+'''/lh.BN_Atlas.annot \
            -f '''+newpath+'''/lh.BN_Atlas.txt \
            -b '''+subID+''' lh
        '''
    incr = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out_V2/sourcedata/freesurfer'';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_anatomical_stats -a '''+newpath+'''/rh.BN_Atlas.annot \
            -f '''+newpath+'''/rh.BN_Atlas.txt \
            -b '''+subID+''' rh
        '''
    incsub = '''
                export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
                export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out_V2/sourcedata/freesurfer'';\
                source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
                mri_segstats --seg ''' + newpath + '''/BN_Atlas_subcotex.mgz \
                --ctab /Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/BN_Atlas_246_LUT.txt \
                --excludeid 0 --sum ''' + newpath + '''/BN_Atlas_subcotex.txt

             '''
    subc14 = '''
                 export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
                 export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out_V2/sourcedata/freesurfer'';\
                 source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
                 asegstats2table --meas volume --tablefile ''' + newpath + '''/subcortialvolume.txt --subjects ''' + i + '/'  '''
               '''
    # os.system(inl)
    # os.system(inr)
    # os.system(incl)
    # os.system(incr)
    # os.system(subint)
    # os.system(incsub)
    os.system(subc14)


