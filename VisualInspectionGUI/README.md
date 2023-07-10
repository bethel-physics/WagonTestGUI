# Visual Inspection GUI

Graphical user interface responsible for running the visual board inspections of both wagons and engines. The interface is largely based on the [HGCAL Tester GUI](https://github.com/UMN-CMS/HGCALTestGUI). Instead of running tests on a wagon/engine test stand, the Visual Inspection GUI utilizes a camera to take a photo of the specified electrical board. This information is then stored in a database for data monitoring. This software is specifically built for use on [Raspberry Pi OS](https://www.raspberrypi.com/software/) but all packages work across Windows and Linux devices with some tweaks.  

## Package Installation
_You must use python3_. To install all of the dependancies for this project, you will need to run the following installation commands. Notice that the versioning for the opencv is important (this is to prevent extensive installation times). 
```
# If permissions denied, add a 'sudo' before each line
pip3 install tkinter
apt-get install python3-pil python3-pil.imagetk
apt  install python3-matplotlib python3-tk
pip3 install pyzmq
pip3 install -U numpy
apt install -y python3-picamera2

# Version type matters here
pip3 install opencv-contrib-python==4.5.3.56 
```



## Running the GUI
After all of the packages have been installed and the camera is plugged into the Raspberry Pi, you will be able to run the program.
```
cd ~/path/to/VisualInspectionGUI
python3 MainFunctionVI.py
```
