#!/usr/bin/env python
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def main():
    omega2 = 10

    theta2 = np.linspace(0, 2*np.pi, num=1000)
    
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
    omega3 = (l[0]*omega2/l[1])*(np.sin(theta4-theta2)/np.sin(theta3-theta4))
    
    a=l[0]
    b=l[1]
    c=l[2]
    d=l[3]

    A_prime = c*np.sin(theta4)
    B_prime = b*np.sin(theta3)
    D_prime = c*np.cos(theta4)
    E_prime = b*np.cos(theta3)
    C_prime = a*(omega2**2)*np.cos(theta2)+b*(omega3**2)*np.cos(theta3)-c*(omega4**2)*np.cos(theta4)
    F_prime = -a*(omega2**2)*np.sin(theta2)-b*(omega3**2)*np.sin(theta3)+c*(omega4**2)*np.sin(theta4)
    
    alpha4 = (C_prime*E_prime-B_prime*F_prime)/(A_prime*E_prime-B_prime*D_prime)

    A_p1 = 48.219*alpha4*(-np.sin(theta4+np.deg2rad(141.067))+1j*np.cos(theta4+np.deg2rad(141.067)))-48.219*(omega4**2)*(np.cos(theta4+np.deg2rad(141.067))+1j*np.sin(theta4+np.deg2rad(141.067)))
    A_p1_mag = np.absolute(A_p1)
   
    A_p1_angle = np.rad2deg(np.angle(A_p1)+np.deg2rad(126.582))

    A_p1_angle[A_p1_angle>100]-=360

    plt.plot(np.rad2deg(theta2), A_p1_angle)
    plt.xlabel('crank angle (deg)')
    plt.ylabel('direction (deg)')
    plt.title('Direction of Ap')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
