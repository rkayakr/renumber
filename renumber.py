#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renumnber V1.0 built on multiPlot v1.2

Renumber version v1.0 reads a node number and then processes files in a list
opening each, processing  and writing data and plot files with the new node number

modified from WWV_plt2.py @authors dkazdan jgibbons
expects a homepath directory with processed files Srawdata 
leaves plot in Renum directory

windows version hardcoded homepath directory location
for Pi comment out windows homepath and uncomment Pi  lines

uses sub_WWV_plt2.py
uses WWV_utility2.py
Bob Benedict, KD8CGH, 7/29/2021

create text file "renumfiles.txt" in homepath directory
  node number
  filename1 
  filename2
  filename3
  ...

Note - expects all data from the same beacon

reads new node number
loads file names in list
for each file
    reads file
    creates data and plot files in Renum directory

uses
WWV_utility2.py
20 February 2020
WWV utility file
Routines and classes used in WWV file management and graphing
David Kazdan, AD8Y
John Gibbons, N8OBJ - mods to plot header 2/3/20

"""

#import os # uncomment for pi
from os import path
import sys
import csv
import math
#import shutil  # uncomment for pi
#from datetime import date, timedelta  # uncomment for pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import filtfilt, butter
import datetime  
from suntime import Sun
from testsub import doplot
from WWV_utility2 import time_string_to_decimals


'''  #uncomment for Pi
# ~ points to users home directory - usually /home/pi/
homepath = os.path.expanduser('~')

# imbed the trailing / in the home path
homepath = homepath + "/PSWS/"

#comment out windows homepath
'''

homepath = "E:\\Documents\\PSWS\\"  # set your windows path, comment out for Pi

names = open(homepath+"renumfiles.txt","r")

Ntemp = names.readline()
NodeNum = Ntemp.strip("\n")
#nn=NodeNum
print(' nodenum ',NodeNum, ' ',len(NodeNum))

if len(NodeNum) != 8:      
    print('Need node number')
    sys.exit(0)

PROCESSDIR = homepath + 'Srawdata/'
RenumDir = homepath + 'Renum/'
#saved plot directrory
PlotDir = homepath + 'Renum/'
XferDir = homepath + 'Renum/'
while True:
    Ftemp = names.readline()
    if  len(Ftemp) <= 1:
        break
    Filename=Ftemp.strip("\n")    
        
    print(Filename)
    
    todofile=(PROCESSDIR + Filename) #with full path
    
    if (path.exists(todofile)):
        print('File ' + todofile + ' found!\nProcessing...')
    else:
        print('File ' + todofile + ' not available.\nExiting disappointed...')
        sys.exit(0)
        
               
    doplot(NodeNum,todofile,PlotDir,XferDir)

