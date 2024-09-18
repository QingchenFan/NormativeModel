import glob
import os.path
from shutil import copy

path = glob.glob('/Volumes/QCII/duilie/duilie_2024512/nifti/V04/*')

for i in path:
    print('i--',i)
    # if 'HC' in i :
    #     subid = i[-8:]
    #     print('subid------',subid)
    #
    #     funcAPpath = glob.glob(i+'/*Functional*AP*5.nii')
    #     funcAPJSONpath = glob.glob(i+'/*Functional*AP*.json')
    #
    #     T1wpath = glob.glob(i+'/*t1*.nii')
    #     T1wJSONpath = glob.glob(i + '/*t1*.json')
    #
    #     fmpath = glob.glob(i+'/*field_mapping*.json')  ##
    #
    #     newpath = '/Volumes/QCII/duilie/BIDS/V4/'+'sub-'+subid
    #     if not os.path.exists(newpath):
    #         os.mkdir(newpath)
    #
    #     funpath = newpath + '/func'
    #     t1wpath = newpath + '/anat'
    #     fieldmappath = newpath + '/fmap'
    #
    #     if not os.path.exists(funpath):
    #         os.mkdir(funpath)
    #     if not os.path.exists(t1wpath):
    #         os.mkdir(t1wpath)
    #     if not os.path.exists(fieldmappath):
    #         os.mkdir(fieldmappath)
    #
    #     for inx, p in enumerate(fmpath):
    #         if 'ph' not in p:
    #             print('p--',p)
    #             n = p.split('/')[-1][:-4]
    #             ph = p[:-5]
    #             inx = inx + 1
    #             fm = ph + '.nii'
    #             print('fm--',fm)
    #             copy(p, fieldmappath + '/sub-' + subid + '_acq-v1_magnitude' + str(inx) + '.json')
    #             copy(fm, fieldmappath + '/sub-' + subid + '_acq-v1_magnitude' + str(inx) + '.nii')
    #         else:
    #             n = p.split('/')[-1][:-5]
    #             ph = p[:-5]
    #             fm = ph + '.nii'
    #             copy(p, fieldmappath + '/sub-' + subid + '_phasediff.json')
    #             copy(fm, fieldmappath + '/sub-' + subid + '_phasediff.nii')
    #
    #     if len(funcAPpath) != 0:
    #         copy(funcAPpath[0],funpath+'/sub-'+subid+'_task-rest_acq-ap_run-1_bold.nii')
    #         copy(funcAPJSONpath[0], funpath + '/sub-' + subid + '_task-rest_acq-ap_run-1_bold.json')
    #     else:
    #         print('No funcAP：',i)
    #
    #     if len(T1wpath) != 0 :
    #         copy(T1wpath[0],t1wpath+'/sub-'+subid+'_T1w.nii')
    #         copy(T1wJSONpath[0], t1wpath + '/sub-' + subid + '_T1w.json')
    #     else:
    #         print('No T1w：', i)

    #
    if 'MDD' in i:

        subid = i[-9:-2] + 'V04'
        print('subid------', subid)

        funcAPpath = glob.glob(i+'/*Functional*AP*5.nii')
        funcAPJSONpath = glob.glob(i+'/*Functional*AP*5.json')

        T1wpath = glob.glob(i+'/*t1*.nii')
        T1wJSONpath = glob.glob(i + '/*t1*.json')
        fmpath = sorted(glob.glob(i + '/*field_mapping*3.5*.json'))
        print('fmpath------', fmpath)

        newpath = '/Volumes/QCII/duilie/BIDS/V4/' + 'sub-' + subid
        if not os.path.exists(newpath):
            os.mkdir(newpath)

        funpath = newpath + '/func'
        t1wpath = newpath + '/anat'
        fieldmappath = newpath + '/fmap'

        if not os.path.exists(funpath):
            os.mkdir(funpath)
        if not os.path.exists(t1wpath):
            os.mkdir(t1wpath)
        if not os.path.exists(fieldmappath):
                os.mkdir(fieldmappath)
        for inx, p in enumerate(fmpath):
            if 'ph' not in p:
                n = p.split('/')[-1][:-5]
                ph = p[:-5]
                inx = inx + 1
                fm = ph + '.nii'
                copy(p, fieldmappath + '/sub-' + subid + '_acq-v1_magnitude' + str(inx) + '.json')
                copy(fm, fieldmappath + '/sub-' + subid + '_acq-v1_magnitude' + str(inx) + '.nii')
            else:
                n = p.split('/')[-1][:-5]
                ph = p[:-5]
                fm = ph + '.nii'
                copy(p, fieldmappath + '/sub-' + subid + '_phasediff.json')
                copy(fm, fieldmappath + '/sub-' + subid + '_phasediff.nii')

        if len(funcAPpath) != 0:
            copy(funcAPpath[0], funpath + '/sub-' + subid + '_task-rest_acq-ap_run-1_bold.nii')
            copy(funcAPJSONpath[0], funpath + '/sub-' + subid + '_task-rest_acq-ap_run-1_bold.json')
        else:
            print('No funcAP：', i)

        if len(T1wpath) != 0:
            copy(T1wpath[0], t1wpath + '/sub-' + subid + '_T1w.nii')
            copy(T1wJSONpath[0], t1wpath + '/sub-' + subid + '_T1w.json')
        else:
            print('No T1w：', i)
    #
    # if 'BP' in i:
    #         subid = i[-9:]
    #         print('subid------', subid)
    #
    #         funcAPpath = glob.glob(i + '/*Functional*AP*.nii')
    #         funcAPJSONpath = glob.glob(i + '/*Functional*AP*.json')
    #
    #         T1wpath = glob.glob(i + '/*t1*.nii')
    #         T1wJSONpath = glob.glob(i + '/*t1*.json')
    #         fmpath = glob.glob(i + '/*field_mapping*.json')  ##
    #
    #         newpath = '/Volumes/QCII/duilie/BIDS/V1/' + 'sub-' + subid
    #         if not os.path.exists(newpath):
    #             os.mkdir(newpath)
    #
    #         funpath = newpath + '/func'
    #         t1wpath = newpath + '/anat'
    #         fieldmappath = newpath + '/fmap'
    #
    #         if not os.path.exists(funpath):
    #             os.mkdir(funpath)
    #         if not os.path.exists(t1wpath):
    #             os.mkdir(t1wpath)
    #         if not os.path.exists(fieldmappath):
    #             os.mkdir(fieldmappath)
    #         for inx,p in enumerate(fmpath):
    #             if 'ph' not in p:
    #                 inx = inx + 1
    #                 n = p.split('/')[-1][:-5]
    #                 ph = p[:-5]
    #                 fm =ph + '.nii'
    #                 copy(p, fieldmappath + '/sub-' + subid + '_acq-v1_magnitude'+str(inx)+'.json')
    #                 copy(fm, fieldmappath + '/sub-' + subid + '_acq-v1_magnitude'+str(inx)+'.nii')
    #         else :
    #                 n = p.split('/')[-1][:-5]
    #                 ph = p[:-5]
    #                 fm = ph + '.nii'
    #                 copy(p, fieldmappath + '/sub-' + subid + '_phasediff.json')
    #                 copy(fm, fieldmappath + '/sub-' + subid + '_phasediff.nii')
    #
    #
    #         if len(funcAPpath) != 0:
    #             copy(funcAPpath[0], funpath + '/sub-' + subid + '_task-rest_acq-ap_run-1_bold.nii')
    #             copy(funcAPJSONpath[0], funpath + '/sub-' + subid + '_task-rest_acq-ap_run-1_bold.json')
    #         else:
    #             print('No funcAP：', i)
    #
    #
    #         if len(T1wpath) != 0:
    #             copy(T1wpath[0], t1wpath + '/sub-' + subid + '_T1w.nii')
    #             copy(T1wJSONpath[0], t1wpath + '/sub-' + subid + '_T1w.json')
    #         else:
    #             print('No T1w：', i)