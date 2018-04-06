#!/usr/bin/env python
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    Rpa = 15
    coord_ang = np.deg2rad(-68.121)

    alpha2 = 10 
    theta2 = np.linspace(np.deg2rad(-26), np.deg2rad(-20.6), num=1000)
    
    l = [9.174, 12.971, 9.573, 7.487]

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

    omega_2 = np.sqrt(2*(theta2-np.deg2rad(-26))*alpha2)
    omega3 = (l[0]*omega_2/l[1])*(np.sin(theta4-theta2)/np.sin(theta3-theta4))
    omega4 = (l[0]*omega_2/l[2])*(np.sin(theta2-theta3)/np.sin(theta4-theta3))

    a=l[0]
    b=l[1]
    c=l[2]
    d=l[3]

    A_A = a*alpha2*(-np.sin(theta2)+1j*np.cos(theta2))-(a*(omega_2**2)*(np.cos(theta2)+1j*np.sin(theta2)))
    
    A_prime = c*np.sin(theta4)
    B_prime = b*np.sin(theta3)
    D_prime = c*np.cos(theta4)
    E_prime = b*np.cos(theta3)
    C_prime = a*alpha2*np.sin(theta2)+a*(omega_2**2)*np.cos(theta2)+b*(omega3**2)*np.cos(theta3)-c*(omega4**2)*np.cos(theta4)
    F_prime = a*alpha2*np.cos(theta2)-a*(omega_2**2)*np.sin(theta2)-b*(omega3**2)*np.sin(theta3)+c*(omega4**2)*np.sin(theta4)
    
    alpha4 = (C_prime*E_prime-B_prime*F_prime)/(A_prime*E_prime-B_prime*D_prime)
    alpha3 = (C_prime*D_prime-A_prime*F_prime)/(A_prime*E_prime-B_prime*D_prime)

    A_p1 = Rpa*alpha3*(-np.sin(theta3))+1j*np.cos(theta3)-Rpa*(omega3**2)*(np.cos(theta3)+1j*np.sin(theta3))

    A_p = A_A + A_p1

    A_p_mag = np.absolute(A_p)
    A_p_angle = np.rad2deg(np.angle(A_p)+np.deg2rad(-68.121))
    A_p_angle[A_p_angle<0]+=360

    plt.plot((np.rad2deg(theta2)), A_p_angle)
    plt.xlabel('theta2 (deg)')
    plt.ylabel('A_p angle (deg)')
    plt.ylim(50,200)
    plt.title('A_p ang v theta2')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
