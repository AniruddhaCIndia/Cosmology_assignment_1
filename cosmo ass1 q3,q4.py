# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 18:39:21 2023

@author: Ayush
"""
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
H0=7.152317880794704e-2 #units in Gyr^{-1} 
omega_m=0.3
omega_r=5*10**(-5)
omega_de=0.7
w=-1.2 #equation of state of dark energy
def f(t,a): #Differential equation to be solved
    dadt=H0*np.sqrt((omega_m/(a))+(omega_r/(a**2))+(omega_de*a**((-3*w)-1)))
    return dadt

#%% Code for question 3
time=np.linspace(0,14,int(1e4))
ainitial=0.0001 #Initial condition
sol=solve_ivp(f, (time[0],time[-1]),[ainitial], method='RK45', t_eval=time)
fig,ax=plt.subplots()
ax.plot(time,sol.y.reshape((10000,)))
ax.set_xlabel(r'time(in Gyrs)')
ax.set_ylabel('a(t)')
ax.set_title(fr'a(t) for $\Omega_m$={omega_m},$\Omega_r$={omega_r},$\Omega_\Lambda$={omega_de} and Dark energy eos (w={w})')

#%% Code for ques 4
a=sol.y.reshape((10000,))
adot=H0*np.sqrt((omega_m/(a))+(omega_r/(a**2))+(omega_de*a**((-3*w)-1))) 
fig2,ax2=plt.subplots()
ax2.plot(time,adot)
ax2.set_xlabel(r'time(in Gyrs)')
ax2.set_ylabel(r'$\dot{a}(t$)')
ax2.set_yscale('log')
ax2.set_title(fr'$\dot a$(t) for $\Omega_m$={omega_m},$\Omega_r$={omega_r},$\Omega_\Lambda$={omega_de} and Dark energy eos (w={w})')
