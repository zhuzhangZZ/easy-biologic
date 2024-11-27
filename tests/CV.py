# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:43:24 2024

@author: Refeyn Ltd
"""

import logging
import easy_biologic as ebl
import easy_biologic.base_programs as ebp
import easy_biologic.program as ep
logging.basicConfig(level=logging.DEBUG)

# create device
bl = ebl.BiologicDevice('USB0')  #IP address is to be confirmed.
bl.connect()

print(bl.info)
print(bl.kind)
# channels to be used
channels = [0]
by_channel = False

# data saving directory
save_path = 'C:\\Data\\Zhu\\EC_lab_test_pyhton\\' # file name is to be defined.
if not by_channel:  
    save_path += 'a5.csv'

# create CV program
params_CV = {
	
    'start': -1.5,
    'E1': -1.5,
    'E2': 2,
    'Ef': 2,
    'vs_initial': False,
    'rate':0.5,                      #unit: V/s
    'step': 0.001,                     #step = dEN/1000
    'N_Cycles': 1,
    'average_over_dE': False, 
    'begin_measuring_I': 0.5,
    'End_measuring_I': 1.0,
    'I_range' : 'KBIO_IRANGE_AUTO',
    'E_range' : 'KBIO_ERANGE_2_5',
    'bandwidth': 'KBIO_BW_5'
}   

CV = ebp.CV(
    bl,
    params_CV,     
    channels = channels,   #channel is to be claimed.
    autoconnect = False)     
# ep.BiologicProgram(bl, params_CV, channels = [1],  autoconnect = False ).channel_state(channels = [1])
# run program
CV.run( 'data' )
CV.save_data(save_path)

# clean up
bl.disconnect()
#cv piture
"""
  
 Ewe ^
     |        E1
     |        /\
     |       /  \        Ef
     |      /    \      /
     |     /      \    /
     |    /        \  /
     |  Ei          \/
     |              E2
     |
     -----------------------> t

"""

import numpy as np
import matplotlib.pyplot as plt
data = np.genfromtxt(save_path, delimiter=',', skip_header=2)
plt.plot(data[:, 0], data[:,1])
