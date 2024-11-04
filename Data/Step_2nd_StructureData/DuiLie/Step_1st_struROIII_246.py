import os
import glob
'''
    因为 fmriprep 运行环境不同，导致输出的 freesurfer结果目录不同，所以写了三个代码来处理
'''

path = '/Volumes/QCII/duilie_processed/duilie_residue_MDD/fmriprep/*/sourcedata/freesurfer'
datapath = glob.glob(path)

for i in datapath:
    print(i)
    subID = i.split('/')[-3]
    print(subID)
    if 'fsaverage' in i:
        continue
    newpath = '/Volumes/QCI/NormativeModel/DuiLie/MDD/DuiLie_Strufeature_Brainnetom/' + subID

    if not os.path.exists(newpath):
        os.mkdir(newpath)

    inl = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=''/Volumes/QCII/duilie_processed/duilie_residue_MDD/fmriprep/'''+subID+'''/sourcedata/freesurfer'';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_ca_label -l $SUBJECTS_DIR/'''+subID+'''/label/lh.cortex.label \
            '''+subID+''' \
            lh $SUBJECTS_DIR/'''+subID+'''/surf/lh.sphere.reg \
            /Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/lh.BN_Atlas.gcs \
            '''+newpath+'''/lh.BN_Atlas.annot
        '''
    inr = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=''/Volumes/QCII/duilie_processed/duilie_residue_MDD/fmriprep/'''+subID+'''/sourcedata/freesurfer'';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_ca_label -l $SUBJECTS_DIR/'''+subID+'''/label/rh.cortex.label \
            '''+subID+''' \
            rh $SUBJECTS_DIR/'''+subID+'''/surf/rh.sphere.reg \
            /Users/qingchen/Documents/Data/template/BrainnetomeAtlas/BN_Atlas_freesurfer/rh.BN_Atlas.gcs \
            '''+newpath+'''/rh.BN_Atlas.annot
        '''
    incl = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=''/Volumes/QCII/duilie_processed/duilie_residue_MDD/fmriprep/'''+subID+'''/sourcedata/freesurfer'';\

            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_anatomical_stats -a '''+newpath+'''/lh.BN_Atlas.annot \
            -f '''+newpath+'''/lh.BN_Atlas.txt \
            -b '''+subID+''' lh 
        '''
    incr = '''
            export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=''/Volumes/QCII/duilie_processed/duilie_residue_MDD/fmriprep/'''+subID+'''/sourcedata/freesurfer'';\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh;\
            mris_anatomical_stats -a '''+newpath+'''/rh.BN_Atlas.annot \
            -f '''+newpath+'''/rh.BN_Atlas.txt \
            -b '''+subID+''' rh 
        '''
    os.system(inl)
    os.system(inr)
    os.system(incl)
    os.system(incr)



