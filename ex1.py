# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 22:03:55 2016
@author: robintiman
"""
from  scipy import *
from  pylab import *

A = set([1,2,3,4,5,6,7])
B = set([1,3,4,9,10])

sumdiff = (A\B).union(B\A)
print(sumdiff)
print(A.symmetric_difference(B))