#!/usr/bin/env python
from __future__ import division
import math
from termcolor import colored
import numpy as np
import matplotlib.pyplot as plt

#theta3_array = np.zeros(10000)
#theta4_array = np.zeros(10000)
X_array = np.zeros(100)
Y_array = np.zeros(100)

def measure_point_displacement_x(theta2, theta3, a, p):
    x = a*np.cos(theta2)+p*np.cos(theta3)
    return x 

def measure_point_displacement_y(theta2, theta3, a, p):
    y = a*np.sin(theta2)+p*np.sin(theta3)
    return y #-y

def fourbar_pose(i, l, theta1, theta2, is_open):
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

    theta4 = 2*np.arctan2((-B-(1*is_open)*np.sqrt(B**2 - 4*A*C)),(2*A))
    theta3 = 2*np.arctan2((-E-(1*is_open)*np.sqrt(E**2 - 4*D*F)),(2*D))

    if theta4 > np.pi*2:
        theta4 = theta4-(2*np.pi)
    elif theta4 < 0:
        theta4 = theta4+(2*np.pi)

    if theta3 > np.pi*2:
        theta3 = theta3-(2*np.pi)
    elif theta3 < 0:
        theta3 = theta3+(2*np.pi)

#    global theta3_array
#    global theta4_array
#    theta3_array = np.insert(theta3_array, i, theta3)
#    theta4_array = np.insert(theta4_array, i, theta4)

    a = l[0]
    p = 1.33
    x = measure_point_displacement_x(theta2, theta3, a, p)
    y = measure_point_displacement_y(theta2, theta3, a, p)
    global X_array
    global Y_array
    X_array = np.insert(X_array, i, x)
    Y_array = np.insert(Y_array, i, y)    

def main():
    theta2_start = math.radians(-120) #-117.037)
    theta2_stop = math.radians(120) #116.037)
    theta2_range = np.linspace(theta2_start, theta2_stop, num=100)

    is_open = 1
    l = [0.86, 1.85, 0.86, 2.22]
    theta1 = 0

    for i in range (0,theta2_range.size):
        fourbar_pose(i, l, theta1, theta2_range[i], is_open)

#    global theta3_array
#    global theta4_array
#    theta3_array = np.delete(theta3_array, range(theta3_array.size-10000, theta3_array.size))
#    theta4_array = np.delete(theta4_array, range(theta4_array.size-10000, theta4_array.size))

#    plt.plot(theta2_range, theta3_array, 'r', label='theta3 displacement')
#    plt.plot(theta2_range, theta4_array, 'g', label='theta4 displacement')
#    plt.legend()
#    plt.xlabel('Theta2 (rads)')
#    plt.ylabel('Displacement (rads)')
#    plt.title('Displacement of Theta3 and Theta4 vs Theta2')
#    plt.grid()
#    plt.show()
    
    global X_array
    global Y_array

#    theta3_array = np.delete(theta3_array, range(theta3_array.size-10000, theta3_array.size))
#    theta4_array = np.delete(theta4_array, range(theta4_array.size-10000, theta4_array.size))

    plt.plot(X_array, Y_array)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Path of Point P')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
