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
Then you need to select the Arrangement type. 
![image](https://github.com/Anson-Jiaqi/Image/blob/main/order_type.png)    

When using command line version, the input example is:  
  
*python Move.py path=D:\example\file target=D:\example\target types=1 x=1 y=1*  
  
"path" is the folder which contain all the image files.  
"target" is the folder where you want to put your Two-level hierarchy folder.  
"types" is the arrangement types.  
"x" and "y" is the coordinates of your image set.


