# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:09:15 2016

@author: savinien
"""

##
#
# build a 20 nodes graph, with two obvious communities (0-9 & 10-19)
#
##


import math
import numpy as np
import scipy as sp

# elementary bloc for communities
bloc = [ [1 for _ in range(10)] for _ in range(10)]
for i, line_i in enumerate(bloc):
    line_i[i]=0

# making the whole graph with two communities based on elementary bloc
graph = [ [0 for _ in range(20)] for _ in range(20)]

for i in range(10):
    graph[i][0:10]=bloc[i]
    graph[i+10][10:20]=bloc[i]

# adding a few inter-community edges
graph[1][12] = 1
graph[12][1] = 1
graph[3][15] = 1
graph[15][3] = 1
graph[6][18] = 1
graph[18][6] = 1


# trivial attributes
attributes = [[0] for _ in range(20)]




