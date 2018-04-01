#!/usr/bin/env python
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    omega2 = -1

    theta2 = np.deg2rad(-26)
    
    l = [9.174, 12.971, 9.573, 7.487]

    k1 = l[3] / l[0]
    k2 = l[3] / l[2]
    k3 = (l[0]**2 - l[1]**2 + l[2]**2 + l[3]**2) / (2*l[0]*l[2])

    A = np.cos(theta2)-k1-k2*np.cos(theta2)+k3
    B = -2*np.sin(theta2)
    C = k1-(k2+1)*np.cos(theta2)+k3

    is_open = -1

    theta4 = 2*np.arctan2((-B-(1*is_open)*np.sqrt(B**2 - 4*A*C)),(2*A)) + 2*np.pi

    k4 = l[3] / l[1]
    k5 = (l[2]**2 - l[3]**2 - l[0]**2 - l[1]**2) / (2*l[0]*l[1])

    D = np.cos(theta2)-k1+k4*np.cos(theta2)+k5
    E = -2*np.sin(theta2)
    F = k1+(k4-1)*np.cos(theta2)+k5
 
    theta3 = 2*np.arctan2((-E-(1*is_open)*np.sqrt(E**2 - 4*D*F)),(2*D)) + 2*np.pi

    omega3 = (l[0]*omega2/l[1])*(np.sin(theta4-theta2)/np.sin(theta3-theta4))
    print "omega3:"
    print omega3
    omega4 = (l[0]*omega2/l[2])*(np.sin(theta2-theta3)/np.sin(theta4-theta3))
    print "omega4:"
    print omega4

    Va = l[0]*omega2*(-np.sin(theta2)+1j*np.cos(theta2))
    Vpa = 15*omega3*(-np.sin(theta3)+1j*np.cos(theta3))
    Vp = Va + Vpa
    Vp_abs = np.absolute(Vp)
    print "Vp_abs:"
    print Vp_abs

if __name__ == '__main__':
    main()
