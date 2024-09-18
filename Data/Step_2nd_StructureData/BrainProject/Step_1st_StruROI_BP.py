import os
import glob


path = '/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/sourcedata/freesurfer/*'
datapath = glob.glob(path)

for i in datapath:

    subID = i.split('/')[-1]
    print(subID)
    if 'fsaverage' in i:
        continue
    newpath = '/home/zhouyuan/fan/Data/brainproject_processed/HC_stru/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)

    ins_r = '''
             export SUBJECTS_DIR=''/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/sourcedata/freesurfer'';\
             mri_surf2surf --hemi rh \
                    --srcsubject fsaverage \
                    --sval-annot /home/zhouyuan/fan/Code/BRAINPREOJECT/annot/rh.Schaefer2018_400Parcels_17Networks_order.annot \
                    --trgsubject '''+subID+''' \
                    --trgsurfval '''+newpath+'''/rh.Schaefer2018_400Parcels_17Networks_ind.annot

             mris_anatomical_stats -a '''+newpath+'''/rh.Schaefer2018_400Parcels_17Networks_ind.annot \
                    -f  '''+newpath+'''/'''+subID+'''_rh.txt \
                    -b '''+subID+''' rh
        '''

    ins_l = '''
             export SUBJECTS_DIR=''/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/sourcedata/freesurfer'';\
             mri_surf2surf --hemi lh \
                    --srcsubject fsaverage \
                    --sval-annot /home/zhouyuan/fan/Code/BRAINPREOJECT/annot/lh.Schaefer2018_400Parcels_17Networks_order.annot \
                    --trgsubject '''+subID+''' \
                    --trgsurfval '''+newpath+'''/lh.Schaefer2018_400Parcels_17Networks_ind.annot

             mris_anatomical_stats -a '''+newpath+'''/lh.Schaefer2018_400Parcels_17Networks_ind.annot \
                    -f  '''+newpath+'''/'''+subID+'''_lh.txt \
                    -b '''+subID+''' lh
        '''
    subc = '''
        export SUBJECTS_DIR=''/home/zhouyuan/fan/Data/brainproject_processed/fmriprep_out_HC/sourcedata/freesurfer'';\
        asegstats2table --meas volume --tablefile '''+newpath+'''/subcortialvolume.txt --subjects '''+i+'''
        '''

    #os.system(ins_r)
    #os.system(ins_l)
    os.system(subc)


