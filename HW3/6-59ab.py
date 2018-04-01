#!/usr/bin/env python
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    mA = np.zeros(100)

    theta2 = np.linspace(math.radians(120-135.069), math.radians(90.5-135.069), num=100)
    
    l = [70, 35, 34, 48]

    k1 = l[3] / l[0]
    k2 = l[3] / l[2]
    k3 = (l[0]**2 - l[1]**2 + l[2]**2 + l[3]**2) / (2*l[0]*l[2])

    k4 = l[3] / l[1]
    k5 = (l[2]**2 - l[3]**2 - l[0]**2 - l[1]**2) / (2*l[0]*l[1])

    A = np.cos(theta2)-k1-k2*np.cos(theta2)+k3
    B = -2*np.sin(theta2)
    C = k1-(k2+1)*np.cos(theta2)+k3

    D = np.cos(theta2)-k1+k4*np.cos(theta2)+k5
    E = -2*np.sin(theta2)
    F = k1+(k4-1)*np.cos(theta2)+k5

    is_open = 1

    theta4 = 2*np.arctan2((-B-(1*is_open)*np.sqrt(B**2 - 4*A*C)),(2*A))
    theta3 = 2*np.arctan2((-E-(1*is_open)*np.sqrt(E**2 - 4*D*F)),(2*D))

    v = theta2 - theta3
    mu = theta4 - theta3

    mA = (l[2]*np.sin(mu)*138)/(l[0]*np.sin(v)*82)

    global_coordinates = np.rad2deg(theta2) + 135.069

    print mA.size
    print mA 
    plt.plot(global_coordinates, mA)
    plt.xlabel('theta 2 (degs)')
    plt.ylabel('mechanical advantage')
    plt.title('theta 2 vs mechanical advantage')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
