#!/usr/bin/env python
from __future__ import division
import math
from termcolor import colored
import numpy as np
import matplotlib.pyplot as plt

X_array = np.zeros(10000)
Y_array = np.zeros(10000)

def measure_point_displacement_x(theta2, theta3, a, p):
    x = a*np.cos(theta2)+p*np.cos(theta3)
    return x 

def measure_point_displacement_y(theta2, theta3, a, p):
    y = a*np.sin(theta2)+p*np.sin(theta3)
    return y

def local_to_global(Rx, Ry, coordinate_angle_displacement):
    X = Rx*np.cos(coordinate_angle_displacement)-Ry*np.sin(coordinate_angle_displacement)
    Y = Rx*np.sin(coordinate_angle_displacement)+Ry*np.cos(coordinate_angle_displacement)
    global X_array
    global Y_array
    X_array = np.append(X_array, X)
    Y_array = np.append(Y_array, Y)

def fourbar_pose(i, l, theta1, theta2, is_open):
    k1 = l[3] / l[0]
    k4 = l[3] / l[1]
    k5 = (l[2]**2 - l[3]**2 - l[0]**2 - l[1]**2) / (2*l[0]*l[1])

    D = np.cos(theta2)-k1+k4*np.cos(theta2)+k5
    E = -2*np.sin(theta2)
    F = k1+(k4-1)*np.cos(theta2)+k5

    theta3 = 2*np.arctan2((-E-(1*is_open)*np.real(np.sqrt(E**2 - 4*D*F))),(2*D))

    a = l[0]
    p = 15.00
    x = measure_point_displacement_x(theta2, theta3, a, p)
    y = measure_point_displacement_y(theta2, theta3, a, p)
    local_to_global(x, y, math.radians(-68.128))

def main():
    theta2_start = math.radians(20.501)
    theta2_stop = math.radians(360)
    theta2_range = np.linspace(theta2_start, theta2_stop, num=10000)

    is_open = -1
    l = [9.174, 12.971, 9.573, 7.487]
    theta1 = 0

    for i in range (0,theta2_range.size):
        fourbar_pose(i, l, theta1, theta2_range[i], is_open)

    plt.plot(X_array, Y_array)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Path of Point P')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
