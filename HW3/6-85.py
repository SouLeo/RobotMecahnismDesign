#!/usr/bin/env python
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    omega2 = 10

    theta2 = np.linspace(np.deg2rad(0-126.582), np.deg2rad(360-126.582), num=1000000)
    
    l = [14, 80, 51.26, 79.701]

    k1 = l[3] / l[0]
    k2 = l[3] / l[2]
    k3 = (l[0]**2 - l[1]**2 + l[2]**2 + l[3]**2) / (2*l[0]*l[2])

    A = np.cos(theta2)-k1-k2*np.cos(theta2)+k3
    B = -2*np.sin(theta2)
    C = k1-(k2+1)*np.cos(theta2)+k3

    is_open = -1

    theta4 = 2*np.arctan2((-B-(1*is_open)*np.sqrt(B**2 - 4*A*C)),(2*A))

    k4 = l[3] / l[1]
    k5 = (l[2]**2 - l[3]**2 - l[0]**2 - l[1]**2) / (2*l[0]*l[1])

    D = np.cos(theta2)-k1+k4*np.cos(theta2)+k5
    E = -2*np.sin(theta2)
    F = k1+(k4-1)*np.cos(theta2)+k5
 
    theta3 = 2*np.arctan2((-E-(1*is_open)*np.sqrt(E**2 - 4*D*F)),(2*D))

    omega4 = (l[0]*omega2/l[2])*(np.sin(theta2-theta3)/np.sin(theta4-theta3))

    e = 48.219
    d_4 = np.deg2rad(136.503)

    Vp = e*omega4*(-np.sin(omega4+d_4)+1j*np.cos(theta4+d_4))
    Vp = np.absolute(Vp)

    theta2_global = theta2 + np.deg2rad(126.582)
    theta2_deg = np.rad2deg(theta2_global)

    plt.plot(theta2_deg, Vp)
    plt.xlabel('theta2 (deg))')
    plt.ylabel('Vp (in/s)')
    plt.title('theta2 vs Vp')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
