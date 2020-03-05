# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:53:20 2020

@author: CIPL
"""

import numpy as np
import matplotlib.pyplot as plt

def PSK(b):
    
    f1=int(input('Enter the frequency of carrier='))
    f2=int(input('Enter the frequency of pulse='))

    A = 5 # amplitude
    t = np.arange(0,1,0.001)
 
    X = A * np.sin(2*np.pi*f1*t)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.title("Carrier")
    plt.plot(t, X)
    plt.show()
    
    u = []#Message signal
    s = 1
    for i in t:
        if i == b[0]:
            b.pop(0)
            if s == 0:
                s = 1
            else:
                s = 0
        u.append(s)
        
    
    plt.plot(t, u)
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Message Signal')
    plt.show()
    
    v = [] #Sine wave multiplied with square wave
    for i in range(len(t)):
        if (u[i]==1):
            v.append(A * np.cos(2 * np.pi * f1 * t[i]))
        else:
            v.append(A * np.cos(2 * np.pi * f1 * t[i])*-1)
        
    plt.plot(t, v)
    plt.grid(True)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("DBPSK")
    plt.show()
    return  v

out = PSK([0.2,0.4,0.6,0.8,1.0])