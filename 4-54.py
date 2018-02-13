#!/usr/bin/env python
from __future__ import division
import math
from termcolor import colored
import numpy as np
import matplotlib.pyplot as plt

link_magnitudes = []
is_open_int = 0
is_ranged = ''
theta1 = 0.0
theta2 = 0.0
theta3_array = np.zeros(100)
theta4_array = np.zeros(100)
#global_theta4_array = np.empty

offset = 0.0

def user_input():
    num_links = raw_input('Please enter how many links are in your system: ')
    if int(num_links) != 4:
        print colored('ERROR: This program only solves 4 bar linkages.', 'red')
        print colored('Restarting program', 'red')
        # TODO: restart program
    else:
        print 'Please enter the link lengths'
        link_a = float(raw_input('link a: '))
        link_b = float(raw_input('link b: '))
        link_c = float(raw_input('link c: '))
        link_d = float(raw_input('link d: '))
        global link_magnitudes 
        link_magnitudes = [link_a, link_b, link_c, link_d]
    print 'Do you want to solve for the open configurations?'
    is_open = raw_input('Enter (Y/n): ')
    global is_open_int
    if is_open == 'Y':
        is_open_int = 1
    else:
        is_open_int = -1
    global is_ranged
    is_ranged = raw_input('Solve for all angles? 0 to 2pi? Y/n ')
        
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

# https://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan2.html

    theta4 = 2*np.arctan2((-B-(1*is_open)*np.sqrt(B**2 - 4*A*C)),(2*A))
    theta3 = 2*np.arctan2((-E-(1*is_open)*np.sqrt(E**2 - 4*D*F)),(2*D))

    global theta3_array
    global theta4_array
    theta3_array = np.insert(theta3_array, i, theta3)
    theta4_array = np.insert(theta4_array, i, theta4)
#    global_theta4 = theta4+offset-2*np.pi
#    global global_theta4_array
#    global_theta4_array = np.append(global_theta4_array, global_theta4)

def local_to_global(Rx, Ry, coordinate_angle_displacement):
    X = Rx*np.cos(coordinate_angle_displacement)-Ry*np.sin(coordinate_angle_displacement)
    Y = Rx*np.sin(coordinate_angle_displacement)+Ry*np.cos(coordinate_angle_displacement)
    global X_array
    global Y_array
    X_array = np.append(X_array, X)
    Y_array = np.append(Y_array, Y)

def measure_point_displacement_x(theta2, theta3, a, p):
    coupler_angle = math.radians(31)
    x = a*np.cos(theta2)+p*np.cos(theta3+coupler_angle)
    return x 

def measure_point_displacement_y(theta2, theta3, a, p):
    coupler_angle = math.radians(31)
    y = a*np.sin(theta2)+p*np.sin(theta3+coupler_angle)
    return y

def magnitude(head, tail):
    magnitude = np.sqrt(np.dot(head, tail))
    return magnitude

def main():
    user_input()    

    global is_ranged
    if is_ranged == 'Y':
        theta2_input_array = np.linspace(0, 2*np.pi, num=100)
        global offset
        offset = math.radians(126.582)
        offset_theta2 = theta2_input_array - offset
        number_of_points = theta2_input_array.size
        for i in range (0, number_of_points):
            fourbar_pose(i, link_magnitudes, theta1, offset_theta2[i], is_open_int)
    else:
        fourbar_pose(link_magnitudes, theta1, theta2, is_open_int)
    global theta3_array
    global theta4_array
#    theta3_array = np.delete(theta3_array, 0)
#    theta4_array = np.delete(theta4_array, 0)
    diff = np.subtract(theta3_array, theta4_array) 
    diff_mag = (diff ** 2)
    diff_mag = diff_mag[diff_mag != 0] 

    print theta2_input_array.size
    print diff_mag 

    plt.plot(theta2_input_array, diff_mag)
    plt.xlabel('Theta2 input angle in radians')
    plt.ylabel('Transmission angle (rad)')
    plt.title('Transmission Angle for B')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
