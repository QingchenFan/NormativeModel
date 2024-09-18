import os
import glob

path = '/Volumes/QCI/HCP/testHCP/*'
datapath = glob.glob(path)

for i in datapath:
    ID = i.split('/')[-1]
    subID = 'sub-' + ID
    if 'fsaverage' in i :
        continue

    newpath = '/Volumes/QCI/HCP/res/' + subID
    if not os.path.exists(newpath):
        os.mkdir(newpath)

    ins = '''
             export SUBJECTS_DIR='/Volumes/QCI/HCP/testHCP/';\
             mri_surf2surf --hemi rh \
                    --srcsubject fsaverage \
                    --sval-annot /Users/qingchen/Documents/code/Data/annot/rh.Schaefer2018_400Parcels_17Networks_order.annot \
                    --trgsubject '''+ID+''' \
                    --trgsurfval '''+newpath+'''/rh.Schaefer2018_400Parcels_17Networks_ind.annot

             mris_anatomical_stats -a '''+newpath+'''/rh.Schaefer2018_400Parcels_17Networks_ind.annot \
                    -f  '''+newpath+'''/'''+subID+'''_rh.txt \
                    -b '''+ID+''' rh
        '''

    os.system(ins)

