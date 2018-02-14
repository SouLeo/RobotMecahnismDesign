#!/usr/bin/env python
from __future__ import division
import math
from termcolor import colored
import numpy as np
import matplotlib.pyplot as plt

def main():
    theta3_range = np.linspace(0, np.pi*2, num=100)
    x = np.zeros(theta3_range.size)
    y = np.zeros(theta3_range.size)
    x = -0.5*np.cos(theta3_range)
    y = 0.5*np.sin(theta3_range)
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Path of Point C')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
