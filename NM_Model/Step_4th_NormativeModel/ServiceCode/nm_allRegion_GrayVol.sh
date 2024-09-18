#!/bin/bash
#SBATCH --job-name=nm
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu 2G
#SBATCH -o /n01dat01/kkwang/HCP/xicang/NormativeModel/Log/job.%j.out
#SBATCH -e /n01dat01/kkwang/HCP/xicang/NormativeModel/Log/job.%j.error.txt
source /n02dat01/public_resource/anaconda3/bin/activate k

python /n01dat01/kkwang/HCP/xicang/NormativeModel/code/nmgpr_allRegion_grayvol.py $1 $2
