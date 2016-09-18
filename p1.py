# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:44:58 2016
@author: robintiman
"""
from  scipy import *
from  pylab import *


class P1:

    def __init__(self):
        knot = [0, 1, 2, 3, 4, 5, 6]
        self.basis_func(knot, 3, 4, 3.4)
        print("hekk")

    # knot vector U = { u0, u1, ..., um }
    def basis_func(knot, k, i, u):
        # Base case
        if (k == 0):
            if knot[i-1] == knot[i]:
                return 0
            elif (u >= knot[i-1] and u < knot[i]):
                return 1
            else:
                return 0

        # Perform the division and set a or b to 0 if division by zero occurs
        try:
            a = (u - knot[i-1]) / (knot[i+k-1] - knot[i-1])
            b = (knot[i+k] - u) / (knot[i+k] - knot[i])
        except ZeroDivisionError:
            if (a):
                b = 0
            elif (b):
                a = 0

        return a * basis_func(knot, k-1, i, u) + b * basis_func(knot, k-1, i+1, u)


