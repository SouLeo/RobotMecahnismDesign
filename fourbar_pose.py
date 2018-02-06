#!/usr/bin/env python
from __future__ import division
import math
from termcolor import colored
import numpy as np

def user_input():
    # collect all link start and end points and if we want
    # open or closed solution, theta1, and theta2
    # have user decide when to stop adding points

    num_links = raw_input('Please enter how many links are in your system: ')
    if (int(num_links) != 4):
        print colored('ERROR: This program only solves 4 bar linkages.', 'red')
        print colored('Restarting program', 'red')
        # TODO: restart program
    else:
        # TODO: Fix entry of links. Input should be: please enter head
        # coordinates and tail coordinates for link a. (then cycle to d)
        print 'Please enter joint positions. Follow this example: '
        print '[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16]]'
        link_joint_poses = input()
        np.array(link_joint_poses)
        print link_joint_poses
        print np.array(link_joint_poses).shape
    print('Do you want to solve for the open configurations?')
    is_open = raw_input('Enter (Y/n): ')
    if is_open == 'Y':
        is_open_int = 1
    else:
        is_open_int = -1
    # TODO: parse raw input to determine if radians or degrees
    theta1 = raw_input('Please enter the constant, theta1, in radians:  ')
    theta2 = raw_input('Please enter the input angle, theta2, in radians: ')
    # TODO: Verifty all inputs are received correctly
    # TODO: Pass input variable information

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

    theta4 = 2*np.arctan((-B-(1*is_open)*np.sqrt(B**2 - 4*A*C))/(2*A))

    theta3 = 2*np.arctan((-E-(1*is_open)*np.sqrt(E**2 - 4*D*F))/(2*D))
    
    print 'theta3 is ' + str(math.degrees(theta3)) + ' degrees'
    print 'theta4 is ' + str(math.degrees(theta4)) + ' degrees'

def magnitude(head, tail):
    magnitude = np.sqrt(np.dot(head, tail))    
    return magnitude

def main():
#    TEST 1: USER INPUT

#    TEST 2: MAGNITUDE FUNCTION
#    head = [1, 2]
#    tail = [3, 4]
#    magnitude(head, tail)

#    TEST 3: POSE CALCULATION
#    l = [40, 120, 80, 100]
#    theta1 = 0
#    theta2 = 0.698132 # 40 degrees
#    is_open = -1
#    fourbar_pose(l, theta1, theta2, is_open)

if __name__ == '__main__':
    main()
