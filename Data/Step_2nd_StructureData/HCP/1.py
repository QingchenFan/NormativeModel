import os
import glob

'''
   使用 Briannetome Atlas 246 对 HCP Data 提取结构指标
'''
path = '/n07dat01/OpenData/HCP1200/*'
path = '/n01dat01/kkwang/HCP/xicang/hcp_T1/*'
datapath = glob.glob(path)

for i in datapath:
    print('i - ', i)
    ID = i.split('/')[-1]
    print('ID - ', ID)
    subID = 'sub-' + ID
    newpath = '/n01dat01/kkwang/HCP/xicang/HCP_Struc_246/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    ep = '/n01dat01/kkwang/HCP/xicang/HCP_Struc_246/' + subID + '/BN_Atlas_subcotex.txt'
    if os.path.exists(ep):
        print("File exist:", ep)
        continue

    # lint = '''
    #         export SUBJECTS_DIR='/n07dat01/OpenData/HCP1200/'''+ID+'''/T1w/';\
    #         mris_ca_label -l $SUBJECTS_DIR/'''+ID+'''/label/lh.cortex.label \
    #         '''+ID+''' lh $SUBJECTS_DIR/'''+ID+'''/surf/lh.sphere.reg \
    #         /n01dat01/kkwang/HCP/xicang/BN_Atlas_freesurfer/lh.BN_Atlas.gcs '''+newpath+'''/lh.BN_Atlas.annot
    #         '''
    #
    # rint = '''
    #         export SUBJECTS_DIR='/n07dat01/OpenData/HCP1200/'''+ID+'''/T1w/';\
    #         mris_ca_label -l $SUBJECTS_DIR/'''+ID+'''/label/rh.cortex.label \
    #         '''+ID+''' rh $SUBJECTS_DIR/'''+ID+'''/surf/rh.sphere.reg  \
    #         /n01dat01/kkwang/HCP/xicang/BN_Atlas_freesurfer/rh.BN_Atlas.gcs '''+newpath+'''/rh.BN_Atlas.annot
    #         '''
    subint = '''
            export SUBJECTS_DIR='/n07dat01/OpenData/HCP1200/''' + ID + '''/T1w/';\
            mri_ca_label $SUBJECTS_DIR/''' + ID + '''/mri/brain.mgz  \
            $SUBJECTS_DIR/''' + ID + '''/mri/transforms/talairach.m3z \
            /n01dat01/kkwang/HCP/xicang/BN_Atlas_freesurfer/BN_Atlas_subcortex.gca \
            ''' + newpath + '''/BN_Atlas_subcotex.mgz
            '''

    # incl = '''
    #         export SUBJECTS_DIR='/n01dat01/kkwang/HCP/xicang/hcp_T1/';\
    #         mris_anatomical_stats -a '''+newpath+'''/lh.BN_Atlas.annot \
    #         -f '''+newpath+'''/lh.BN_Atlas.txt \
    #         -b '''+ID+''' lh
    #     '''
    #
    #
    # incr = '''
    #         export SUBJECTS_DIR='/n01dat01/kkwang/HCP/xicang/hcp_T1/';\
    #         mris_anatomical_stats -a '''+newpath+'''/rh.BN_Atlas.annot \
    #         -f '''+newpath+'''/rh.BN_Atlas.txt \
    #         -b '''+ID+''' rh
    #     '''
    incsub = '''
                export SUBJECTS_DIR='/n01dat01/kkwang/HCP/xicang/hcp_T1/';\
                mri_segstats --seg ''' + newpath + '''/BN_Atlas_subcotex.mgz \
                --ctab /n01dat01/kkwang/HCP/xicang/BN_Atlas_freesurfer/BN_Atlas_246_LUT.txt \
                --excludeid 0 --sum ''' + newpath + '''/BN_Atlas_subcotex.txt

             '''
    # os.system(lint)
    # os.system(rint)
    os.system(subint)
    # os.system(incl)
    # os.system(incr)
    os.system(incsub)


