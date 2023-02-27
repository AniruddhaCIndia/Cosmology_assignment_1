# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 22:45:55 2023

@author: Ayush
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
H0=10 #units in km/s/Mpc
sigma=300 #units in km/s
sample_length=int(1e2)
d=100*np.random.random(sample_length) #randomly picking up distance of galaxies
vp=np.random.normal(0,sigma,sample_length)
v=(H0*d)+vp
plt.plot(d,v,'.')
plt.xlabel('distance d(in Mpc)')
plt.ylabel('Velocity v(in Km/s)')
plt.suptitle(f'Plot of v vs d for {sample_length} galaxies')
plt.title(fr'$H_0=${H0} Km/s/Mpc , $\sigma=${sigma} Km/s')

