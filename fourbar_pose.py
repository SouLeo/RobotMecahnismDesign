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
X_array = np.empty
Y_array = np.empty

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
#    is_rad = raw_input('Do you want to enter the input angles in radians? (Y/n): ')
#    global theta1
#    global theta2
#    if is_rad == 'Y':
#        theta1 = float(raw_input('Please enter the constant, theta1, in radians:  '))
#        theta2 = float(raw_input('Please enter the input angle, theta2, in radians: '))
#    else:
#        theta1 = math.radians(float(raw_input('Please enter the constant, theta1, in degrees:  ')))
#        theta2 = math.radians(float(raw_input('Please enter the input angle, theta2, in degrees: ')))
        
def fourbar_pose(l, theta1, theta2, is_open):
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
    
    p = 3.06

    Rx = measure_point_displacement_x(theta2, theta3, l[0], p)
    Ry = measure_point_displacement_y(theta2, theta3, l[0], p)
    
    coordinate_angle_displacement = math.radians(25)

    local_to_global(Rx, Ry, coordinate_angle_displacement)

#    print 'theta3 is ' + str(math.degrees(theta3)) + ' degrees'
#    print 'theta4 is ' + str(math.degrees(theta4)) + ' degrees'

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
#    TEST 1: USER INPUT
    user_input()    
#    TEST 2: MAGNITUDE FUNCTION
#    head = [1, 2]
#    tail = [3, 4]
#    magnitude(head, tail)

#    TEST 3: POSE CALCULATION

    global is_ranged
    if is_ranged == 'Y':
        theta2_input_array = np.linspace(0, 2*np.pi, num=100)
        number_of_points = theta2_input_array.size
        for i in range (0, number_of_points):
            fourbar_pose(link_magnitudes, theta1, theta2_input_array[i], is_open_int)
    else:
        fourbar_pose(link_magnitudes, theta1, theta2, is_open_int)
    global X_array
    global Y_array
#    print 'X_array: '
#    print(X_array)
#    print 'Y_array: '
#    print(Y_array)
    X_array = np.delete(X_array, 0)
    Y_array = np.delete(Y_array, 0)
    plt.plot(X_array, Y_array)    
    plt.xlabel('X displacement in units')
    plt.ylabel('Y displacement in units')
    plt.title('XY Displacement in Walking Beam Mechanism. Assume Global v Local displacement is 25 degrees')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
