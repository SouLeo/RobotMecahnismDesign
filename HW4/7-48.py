#!/usr/bin/env python
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    a = 0.8
    a_prime = 2.97
    b_prime = 2.61
    c_prime = 3.25
    d = 1.85
    
    
    theta_2 = np.deg2rad(-37.5)
    
    beta = np.deg2rad(-81.5)
    
    omega_2 = 40/60
    alpha_2 = -1500/3600

    coord_ang = np.deg2rad(-90)
 
    theta_3 = np.arctan2(a*np.sin(theta_2), a*np.cos(theta_2)-d)

    b = (a*np.sin(theta_2))/np.sin(theta_3)

    omega_3 = (a*omega_2/b)*np.cos(theta_2-theta_3)

    b_dot = (a*omega_2*np.cos(theta_2)-b*omega_3*np.cos(theta_3))/np.sin(theta_3)

    alpha_3 = (1/b)*(a*alpha_2*np.cos(theta_2-theta_3)+a*(omega_2**2)*np.sin(theta_3-theta_2)-2*b_dot*omega_3)

    A_A = a*alpha_2*(-np.sin(theta_2)+1j*np.cos(theta_2))-(a*(omega_2**2)*(np.cos(theta_2)+1j*np.sin(theta_2)))
    print "A_A mag and angle"
    print np.absolute(A_A)
    print np.rad2deg(np.angle(A_A))

    theta_3_glob = theta_3+2*np.pi+beta
    A_B = a_prime*alpha_3*(-np.sin(theta_3_glob)+1j*np.cos(theta_3_glob))-a_prime*(omega_3**2)*(np.cos(theta_3_glob)+1j*np.sin(theta_3_glob))
    print "A_B mag and angle"
    print np.absolute(A_B)
    print np.rad2deg(np.angle(A_B))

    theta_5 = np.arcsin((-a_prime*np.sin(theta_3_glob)+c_prime)/b_prime)+np.pi
    omega_5 = (a_prime/b_prime)*(np.cos(theta_3_glob)/np.cos(theta_5))*omega_3
    alpha_5 = (a_prime*alpha_3*np.cos(theta_3_glob)-a_prime*(omega_3**2)*np.sin(theta_3_glob)+b_prime*(omega_5**2)*np.sin(theta_2))/(b_prime*np.cos(theta_5))

    A_C = -a_prime*alpha_3*np.sin(theta_3_glob)-a_prime*(omega_3**2)*np.cos(theta_3_glob)+b_prime*(alpha_5)*np.sin(theta_5)+b_prime*(omega_5**2)*np.cos(theta_5)
    print "A_C mag and angle"
    print np.absolute(A_C)
    print np.rad2deg(np.angle(A_C))

if __name__ == '__main__':
    main()
