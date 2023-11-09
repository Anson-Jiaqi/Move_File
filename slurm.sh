#!/bin/bash
#SBATCH --time=00:15:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=3   # number of nodes
#SBATCH --ntasks-per-node=1   # 1 processor core(s) per node 
#SBATCH --gres=gpu:1
#SBATCH --partition=vgpu20    # gpu node(s)
#SBATCH --job-name="test"

# The following is exactly the same as we did before, load up enviroment and run the code.

# Link the path to miniconda's binaries (created by conda installer)

export PATH="/home/Student/s4733108/miniconda3/bin:$PATH"
export PATH="/home/Student/s4733108/TeraStitcher2:$PATH"
ml mpi/latest

# export LD_LIBRARY_PATH=/home/Student/s4733108/openmpi/lib:$LD_LIBRARY_PATH
# export PATH="/home/Student/s4733108/openmpi/bin:$PATH"

#Use CUDA
# export USECUDA_X_NCC=1

# step 1, Replace Your foder Path after "--volin="
terastitcher -1 --volin=Your Path --projout=xml_import.xml  --ref1=1 --ref2=2 --ref3=3 --vxl1=0.65 --vxl2=0.65 --vxl3=4.9 --volin_plugin="TiledXY|2Dseries"
# step 2, Use "mpiexec" on Windows
mpirun -np 3 python parastitcher.py -2 --projin=./xml_import.xml --projout=./xml_displcomp_par.xml --sV=58 --sH=33 --sD=0 --oV=204 --oH=204 > ./step2par.txt
# step 3
terastitcher -3 --projin=./xml_displcomp_par.xml --projout=disp.xml
# step 4
terastitcher -4 --projin=./disp.xml --projout=./thrdisp.xml --threshold=0
# step 5
terastitcher -5 --projin=./thrdisp.xml --projout=./place.xml --algorithm=MIPNCC
# step 6, Use "mpiexec" on Windows, Replace Your target foder Path after "--volout="
mpirun -np 3 python ./parastitcher.py -6 --projin=./place.xml --volout_plugin="TiledXY|3Dseries" --volout=Target Path --resolutions=0 --slicewidth=4096 --sliceheight=4096 --slicedepth=10 > ./step6par.txt