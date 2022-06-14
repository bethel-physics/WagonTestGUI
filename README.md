


# WagonTestGUI

This repository contains the GUI used to run the quality control testing for all HGCAL LD Wagons.

## Setup 

Run these commands from your working area to pull the code in:

    git clone git@github.com:UMN-CMS/WagonTestGUI.git
    
When updating the code, you can use the following commands:
    
    git add <your files>
    git commit -m "Message about what you are committing"
    git push origin <LocalBranchName>:<RemoteBranchName>
    
You can then open a pull request (PR) by going to the Github repo and then we can merge your code into the master branch. 

## To run the program:

To run the program:

Open files in VS Code (or any application that runs Python) and run the following commands in the terminal:

``` 
python -m venv virtenv 

virtenv/Scripts/activate

pip -m install requests.txt

python ./MainFunction.py
```


## Goals for this Framework:

The main goal for this framework is to have an efficient and easy-to-use user interface for running Wagon QC testing. The points of focus are:
- Integration the GUI with the test results database to store information about which boards have been tested and what tests have been run
- Easy to understand step-by-step instructions for QC testers to follow
- Implementation of a barcode scanning functionality for registering new boards and uploading test results
- Tracking of who is doing a tests, where it is taking place, and where the boards will be moved to after testing is finished

## Background Information

### What is a GUI?

A GUI (or Graphical User Interface) is a program which allows users to interact with software via buttons, text entry boxes, and other module types. Most software that we are familiar with includes a user interface where we can modify data, navigate pages, and perform actions. An example of a GUI is the webpage you are currently on! You can choose to look at some of the code in this repository or perform actions to updated it with the click of a button. 

The GUI we will be developing for testing wagon functionality will be python based. There are a few packages that can be used for developing python based GUIs. The example GUI ([here](gui/initial_test_gui.py)) uses [TKinter](https://docs.python.org/3/library/tkinter.html) to produce the user interface. You can try out this GUI by performing the following command line call: `python initial_test_gui.py`.

### What is a Wagon?

Wagons are the motherboard connecting the active detector modules (what is measuring particle intractions) and the engines (the "brains" of the front-end electronics). Wagons are responsible for carrying clock, trigger, DAQ, and control infromation to between 2-4 modules simultaneously. They are completely passive boards and have no chips for communicating with the rest of the system. 

The purpose of wagons in the front-end readout train is to tranasmit data and control information to and from modules. Thus, we would like to ensure that each wagon in the final version of the detector has been checked for good communication ability.

### What tests are being run?

There are four tests that need to be run in order to verify a wagon is funcitioning properly:

- Analog line connection check: measure the resistance of each of the analog lines on the wagon to ensure good connection
- Measurement of ID resistor: each wagon has a precision resistor used for identification of wagon type that must be measured and compared to the nominal value
- I2C read/write test: verify that the slow control communication along the wagon lines is working
- Bit error rate measurement: check the quality of the data sent along the wagon elinks