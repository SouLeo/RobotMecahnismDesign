#!/usr/bin/env python
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    omega2 = -1

    theta2 = np.linspace(0, 2*np.pi, num=1000)
    
    l = [2.170, 2.067, 2.310, 1.000, 5.40]

    k1 = l[3] / l[0]
    k2 = l[3] / l[2]
    k3 = (l[0]**2 - l[1]**2 + l[2]**2 + l[3]**2) / (2*l[0]*l[2])

    A = np.cos(theta2)-k1-k2*np.cos(theta2)+k3
    B = -2*np.sin(theta2)
    C = k1-(k2+1)*np.cos(theta2)+k3

    is_open = 1

    theta4 = 2*np.arctan2((-B-(1*is_open)*np.sqrt(B**2 - 4*A*C)),(2*A)) - np.deg2rad(102)
    
    theta4[theta4>(2*np.pi)]-=2*np.pi
    theta4[theta4<0]+=2*np.pi

    print theta4

    theta5 = np.arcsin((-l[2]*np.sin(theta4))/l[4]) + np.pi
    f = l[2]*np.cos(theta4)-l[4]*np.cos(theta5)
    
    k4 = l[3] / l[1]
    k5 = (l[2]**2 - l[3]**2 - l[0]**2 - l[1]**2) / (2*l[0]*l[1])

    D = np.cos(theta2)-k1+k4*np.cos(theta2)+k5
    E = -2*np.sin(theta2)
    F = k1+(k4-1)*np.cos(theta2)+k5
 
    theta3 = 2*np.arctan2((-E-(1*is_open)*np.sqrt(E**2 - 4*D*F)),(2*D))

    omega4 = (l[0]*omega2/l[2])*(np.sin(theta2-theta3)/np.sin(theta4+1.78024-theta3))
    omega5 = (l[2]/l[4])*(np.cos(theta4)/np.cos(theta5))*omega4

    Vc = -l[2]*omega4*np.sin(theta4)+l[4]*omega5*np.sin(theta5)

    theta2_deg = np.rad2deg(theta2)

    plt.plot(f, Vc)
    plt.xlabel('slider pose (units)')
    plt.ylabel('Vc (units/s)')
    plt.title('slider pose vs Vc')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
