#!/usr/bin/env python
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    a=105
    b=172
    c=27
    
    mA = np.zeros(100)

    theta_2 = np.linspace(math.radians(15), math.radians(60), num=100) 

    theta_3 = np.arcsin((a*np.sin(theta_2)-c)/b)+np.pi
    omega_3 = (a/b)*(np.cos(theta_2)/np.cos(theta_3))*1

    Vd = np.absolute(-a*1*np.sin(theta_2)+b*omega_3*np.sin(theta_3))
    Vc = 301
    
    mA = Vc/Vd

    print mA 
    plt.plot(theta_2, mA)
    plt.xlabel('theta 2 (radians)')
    plt.ylabel('mechanical advantage')
    plt.title('theta 2 vs mechanical advantage')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
