'''
testsub


'''
import os
from os import path
import sys
import csv
import shutil
from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend, show, grid, figure, savefig
from scipy.signal import filtfilt, butter
import subprocess
from WWV_utility2 import time_string_to_decimals, graph_Doppler_and_power_data
import maidenhead as mh


def dofile(fname):
    print(' in test ',fname,'\n')
    
    with open(fname, 'r') as dataFile:
        dataReader=csv.reader(dataFile)
        data = list(dataReader)
        Header = data.pop(0)

