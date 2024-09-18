import os
import glob
os.system(' export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=/Applications/freesurfer/7.4.1/subjects;\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh ;  '
          )

path = '/Volumes/QCII/Data135_processed/data135_HC_fmriprep_out/sourcedata/freesurfer/*'
datapath = glob.glob(path)

for i in datapath:

    subID = i.split('/')[-1]
    print(subID)
    if 'fsaverage' in i:
        continue
    newpath = '/Volumes/QCI/NormativeModel/Data135/HC/Strufeature/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)

    ins_r = '''export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
             export SUBJECTS_DIR=/Applications/freesurfer/7.4.1/subjects;\
             source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh ;    \
             export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_HC_fmriprep_out/sourcedata/freesurfer'';\
             mri_surf2surf --hemi rh \
                    --srcsubject fsaverage \
                    --sval-annot /Users/qingchen/Documents/code/Data/annot/rh.Schaefer2018_400Parcels_17Networks_order.annot \
                    --trgsubject '''+subID+''' \
                    --trgsurfval '''+newpath+'''/rh.Schaefer2018_400Parcels_17Networks_ind.annot

             mris_anatomical_stats -a '''+newpath+'''/rh.Schaefer2018_400Parcels_17Networks_ind.annot \
                    -f  '''+newpath+'''/'''+subID+'''_rh.txt \
                    -b '''+subID+''' rh
        '''

    ins_l = '''export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
             export SUBJECTS_DIR=/Applications/freesurfer/7.4.1/subjects;\
             source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh ;    \
             export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_HC_fmriprep_out/sourcedata/freesurfer'';\
             mri_surf2surf --hemi lh \
                    --srcsubject fsaverage \
                    --sval-annot /Users/qingchen/Documents/code/Data/annot/lh.Schaefer2018_400Parcels_17Networks_order.annot \
                    --trgsubject '''+subID+''' \
                    --trgsurfval '''+newpath+'''/lh.Schaefer2018_400Parcels_17Networks_ind.annot

             mris_anatomical_stats -a '''+newpath+'''/lh.Schaefer2018_400Parcels_17Networks_ind.annot \
                    -f  '''+newpath+'''/'''+subID+'''_lh.txt \
                    -b '''+subID+''' lh
        '''
    subc = '''
         export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
         export SUBJECTS_DIR=/Applications/freesurfer/7.4.1/subjects;\
         source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh ;    \
         export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_HC_fmriprep_out/sourcedata/freesurfer'';\
         asegstats2table --meas volume --tablefile ''' + newpath + '''/subcortialvolume.txt --subjects ''' + i + '''
         '''

    os.system(ins_r)
    os.system(ins_l)
    os.system(subc)
    exit()




