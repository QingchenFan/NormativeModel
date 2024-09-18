import os
import glob
os.system(' export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
            export SUBJECTS_DIR=/Applications/freesurfer/7.4.1/subjects;\
            source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh ;  '
          )

path = '/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out/fmriprep/*/sourcedata/freesurfer'
datapath = glob.glob(path)

for i in datapath:
    subID = i.split('/')[-3]
    newpath = '/Volumes/QCI/NormativeModel/Data135/MDD/Strufeature/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)

    inr = '''export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
             export SUBJECTS_DIR=/Applications/freesurfer/7.4.1/subjects;\
             source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh ;    \
             export SUBJECTS_DIR='/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out/fmriprep/'''+subID+'''/sourcedata/freesurfer';\
             mri_surf2surf --hemi rh \
                    --srcsubject fsaverage \
                    --sval-annot /Users/qingchen/Documents/code/Data/annot/rh.Schaefer2018_400Parcels_17Networks_order.annot \
                    --trgsubject '''+subID+''' \
                    --trgsurfval '''+newpath+'''/rh.Schaefer2018_400Parcels_17Networks_ind.annot

             mris_anatomical_stats -a '''+newpath+'''/rh.Schaefer2018_400Parcels_17Networks_ind.annot \
                    -f  '''+newpath+'''/'''+subID+'''_rh.txt \
                    -b '''+subID+''' rh
        '''
    inl = '''export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
              export SUBJECTS_DIR=/Applications/freesurfer/7.4.1/subjects;\
              source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh ;    \
              export SUBJECTS_DIR='/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out/fmriprep/''' + subID + '''/sourcedata/freesurfer';\
              mri_surf2surf --hemi lh \
                     --srcsubject fsaverage \
                     --sval-annot /Users/qingchen/Documents/code/Data/annot/lh.Schaefer2018_400Parcels_17Networks_order.annot \
                     --trgsubject ''' + subID + ''' \
                     --trgsurfval ''' + newpath + '''/lh.Schaefer2018_400Parcels_17Networks_ind.annot

              mris_anatomical_stats -a ''' + newpath + '''/lh.Schaefer2018_400Parcels_17Networks_ind.annot \
                     -f  ''' + newpath + '''/''' + subID + '''_lh.txt \
                     -b ''' + subID + ''' lh
         '''
    subc = '''
           export FREESURFER_HOME=/Applications/freesurfer/7.4.1; \
           export SUBJECTS_DIR=/Applications/freesurfer/7.4.1/subjects;\
           source /Applications/freesurfer/7.4.1/SetUpFreeSurfer.sh ;    \
           export SUBJECTS_DIR=''/Volumes/QCII/Data135_processed/data135_MDD_fmriprep_out/fmriprep/''' + subID + '''/sourcedata/freesurfer'';\
           asegstats2table --meas volume --tablefile ''' + newpath + '''/subcortialvolume.txt --subjects ''' + i + '/' + subID + '''
           '''
    # os.system(inr)
    # os.system(inl)
    os.system(subc)

