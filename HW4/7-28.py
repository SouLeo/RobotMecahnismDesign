#!/usr/bin/env python
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    a = 63
    b = 130
    c = -52
    
    theta_2 = np.deg2rad(141)
    omega_2 = -25
    alpha_2 = 0

    coord_ang = np.deg2rad(-90)
 
    theta_3 = np.arcsin((a*np.sin(theta_2)-c)/b)
    d = a*np.cos(theta_2)-b*np.cos(theta_3)
    omega_3 = (a/b)*(np.cos(theta_2)/np.cos(theta_3))*omega_2

    A_A = a*alpha_2*(-np.sin(theta_2)+1j*np.cos(theta_2))-a*(omega_2**2)*(np.cos(theta_2)+1j*np.sin(theta_2))
    A_A_mag = np.absolute(A_A)
    A_A_ang = np.angle(A_A)

    print A_A_mag
    print np.rad2deg(A_A_ang+coord_ang)

    alpha_3 = (a*alpha_2*np.cos(theta_2)-a*(omega_2**2)*np.sin(theta_2)+b*(omega_3**2)*np.sin(theta_3))/(b*np.cos(theta_3))
    A_B = -a*alpha_2*np.sin(theta_2)-a*(omega_2**2)*np.cos(theta_2)+b*alpha_3*np.sin(theta_3)+b*(omega_3**2)*np.cos(theta_3)
    A_B_mag = np.absolute(A_B)
    A_B_ang = np.angle(A_B)

    print A_B_mag
    print np.rad2deg(A_B_ang)

if __name__ == '__main__':
    main()
