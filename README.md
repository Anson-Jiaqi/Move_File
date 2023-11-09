# Move_File
This tool is to move the files to the Two-level hierarchy folder so that it can import into the Terastitcher.  
It will generate the Two-level hierarchy folder for each channel.  
There are two version.   
Move.py is use with command line.  
Move_gui.py is a GUI version.  
You need to input the X and Y of your dataset.  
All files should under one folder, and should only include the file you want to use.The total file number should equal to X*Y  
Your file name should include XXX_F123_C123_Z123.tif   
F123 is the file order, "F" or "f" followed by any number.  
C123 is the channel, "C" or "c"followed by any number.  
Z123 is the Z layer, "Z" or "z"followed by any number.  
Example file name:  
  
NewFilename_561nm_A568_Confocal_40um_Zyla-1_488nm_GFP_Confocal...ocal_40um_Zyla-2_2023-08-02_12.18.30_F0_t001_z001_c001.tif  

Then you need to select the Arrangement type. 
![image](https://github.com/Anson-Jiaqi/Image/blob/main/order_type.png)    

When using command line version, the input example is:  
  
    python Move.py path=D:\example\file target=D:\example\target types=1 x=1 y=1  
  
"path" is the folder which contain all the image files.  
"target" is the folder where you want to put your Two-level hierarchy folder.  
"types" is the arrangement types.  
"x" and "y" are the coordinates of your image set.

# Using Terastitcher  
# step 1
    terastitcher -1 --volin=Your Path --projout=xml_import.xml  --ref1=1 --ref2=2 --ref3=3 --vxl1=0.65 --vxl2=0.65 --vxl3=4.9 --volin_plugin="TiledXY|2Dseries"  
--volin: the two level hierarchy folder  
############################################  
--ref1: First axis of the used reference system  
--ref2:	Second axis of the used reference system  
--ref3: Third axis of the used reference system  
Y or V or 1 for the vertical axis  
X or H or 2 for the horizontal axis  
Z or D or 3 for the depth axis  
############################################  
--vxl1: Voxel size along first axis (in microns*).  
--vxl2: Voxel size along second axis (in microns*).  
--vxl3: Voxel size along third axis (in microns*).  
############################################  
--volin_plugin  
Plugin that manages the input volume format. Available plugins are:  
  
TiledXY|2Dseries  
TiledXY|3Dseries  
Default is TiledXY|2Dseries.  
############################################  
  
  
## step 2  
Sequential execution:  

    terastitcher -2 --projin=./xml_import.xml --projout=./xml_displcomp_par.xml --sV=25 --sH=25 --sD=25 --oV=204 --oH=204  
MPI version:  

    mpirun -np 3 python parastitcher.py -2 --projin=./xml_import.xml --projout=./xml_displcomp_par.xml --sV=25 --sH=25 --sD=25 --oV=204 --oH=204> ./step2par3.txt  
  
-np: Number of the node. At least 2 nodes. On windows is "mpiexec" instead of "mpirun"  
parastitcher.py -2 means step 2  
--projin: Input file  
--projout: Output file  
############################################  
--sV: Radius of search (in pixels) for displacements computation along axis V(Y) . The higher the radius, the more computation is done.  
--sH: Radius of search (in pixels) for displacements computation along axis H(X) . The higher the radius, the more computation is done.  
--sD: Radius of search (in pixels) for displacements computation along axis D(Z) . The higher the radius, the more computation is done.  
Just set it to default(25 pixels) is ok  
############################################  
--oV: Overlap in V(X)  
--oH: Overlap in H(Y)  
  
## step 3  
    terastitcher -3 --projin=./xml_displcomp_par.xml --projout=disp.xml  
--projin: Input file  
--projout: Output file  

## step 4  
    terastitcher -4 --projin=./disp.xml --projout=./thrdisp.xml --threshold=0  
--projin: Input file  
--projout: Output file  
  
## step 5  
    terastitcher -5 --projin=./thrdisp.xml --projout=./place.xml  
--projin: Input file  
--projout: Output file  
  
## step 6 
Sequential execution:  

    terastitcher -6 --projin=./place.xml --volout_plugin="TiledXY|3Dseries" --volout=Target Path --resolutions=0 --slicewidth=4096 --sliceheight=4096 --slicedepth=10 

MPI version:  

    mpirun -np 3 python ./parastitcher.py -6 --projin=./place.xml --volout_plugin="TiledXY|3Dseries" --volout=Target Path --resolutions=0 --slicewidth=4096 --sliceheight=4096 --slicedepth=10  
On windows is "mpiexec" instead of "mpirun"   
--projin: Input file  
--volout_plugin: Output format.  
Available plugins are:  
  
TiledXY|2Dseries  
TiledXY|3Dseries  
Default is TiledXY|2Dseries.  
--volout: Output folder path  
--resolutions: Resolutions to be produced. Possible values are [[i]...] where i = 0,..,10 and 2^i is the subsampling factor.   
Default is 0, that means that only the highest resolution (subsampling factor 2^0=1) will be produced.  

--slicewidth: Supposing the output image is saved in a tiled format, this is the width of output tiles.  
--sliceheight: Supposing the output image is saved in a tiled format, this is the height of output tiles.  
--slicedepth: Supposing the output image is saved in a format supporting 3D-tiling, this is the dimension of tiles in Z(D).  
Can not set to default! Because default is -1, it will cause problem when using Terastitcher.  
You can simply compute it. For exapmle, if the image is X=2,Y=4,Z=10, each image is 2048*2048. Then --slicewidth=2048*2 --sliceheight=4096 --slicedepth=10  
The final output may smaller than these number because there are overlap. But make sure the number you input is bigger than the real size.  


For Terastitcher set up and more detail, you can check here:   
https://github.com/abria/TeraStitcher/wiki  

#  Try  
1, Download the demo image:  
https://www.dropbox.com/scl/fi/bakiyrk9frdr8kylbt4jt/demo_image.zip?rlkey=umlqgt2bwxms5gbuekjs3d6av&dl=0  
It is a 2*2 and 2 channels image, X=2, Y=2, Z=10. Arrangement type is: type 1
  
2, Set up Terastitcher and environment according to: https://github.com/abria/TeraStitcher/wiki/Multi-CPU-parallelization-using-MPI-and-Python-scripts  

3, Download the parastitcher.py script.  
  
4, Use Move.py or Move_gui.py to create two level hierarchy folder.  
If using command line version, use the command:

    python Move.py path=D:\example\file target=D:\example\target types=1 x=2 y=2
Replace path to your path, and target to your target folder.  
When finished, you will see two folder, C1 and C2. Each folder stands for each channel.  

5, Move the parastitcher.py script in to C1 or C2 folder.  
Start and use Terastitcher according to ***Using Terastitcher***  

6, Try it on HPC cluster  
Download the Slurm.sh script, or you can create your own.  






