import os
import glob
'''
   使用 Briannetome Atlas 246 对 HCP Data 提取结构指标
'''
path = '/n07dat01/OpenData/HCP1200/*'
datapath = glob.glob(path)

for i in datapath:
    print('i - ',i)
    ID = i.split('/')[-1]
    print('ID - ',ID)
    subID = 'sub-' + ID
    newpath = '/n01dat01/kkwang/HCP/xicang/HCP_Struc_246/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)

    lint = '''
            export SUBJECTS_DIR='/n07dat01/OpenData/HCP1200/'''+ID+'''/T1w/';\
            mris_ca_label -l $SUBJECTS_DIR/'''+ID+'''/label/lh.cortex.label \
            '''+ID+''' lh $SUBJECTS_DIR/'''+ID+'''/surf/lh.sphere.reg \
            /n01dat01/kkwang/HCP/xicang/BN_Atlas_freesurfer/lh.BN_Atlas.gcs '''+newpath+'''/lh.BN_Atlas.annot
            '''

    rint = '''
            export SUBJECTS_DIR='/n07dat01/OpenData/HCP1200/'''+ID+'''/T1w/';\
            mris_ca_label -l $SUBJECTS_DIR/'''+ID+'''/label/rh.cortex.label \
            '''+ID+''' rh $SUBJECTS_DIR/'''+ID+'''/surf/rh.sphere.reg  \
            /n01dat01/kkwang/HCP/xicang/BN_Atlas_freesurfer/rh.BN_Atlas.gcs '''+newpath+'''/rh.BN_Atlas.annot
            '''
    incl = '''
            export SUBJECTS_DIR='/n07dat01/OpenData/HCP1200/'''+ID+'''/T1w/';\
            mris_anatomical_stats -a '''+newpath+'''/lh.BN_Atlas.annot \
            -f '''+newpath+'''/lh.BN_Atlas.txt \
            -b '''+ID+''' lh 
        '''
    incr = '''
            export SUBJECTS_DIR='/n07dat01/OpenData/HCP1200/'''+ID+'''/T1w/';\
            mris_anatomical_stats -a '''+newpath+'''/rh.BN_Atlas.annot \
            -f '''+newpath+'''/rh.BN_Atlas.txt \
            -b '''+ID+''' rh 
        '''
    # os.system(lint)
    # os.system(rint)
    os.system(incl)
    os.system(incr)
    exit()