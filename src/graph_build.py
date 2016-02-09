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


# elementary bloc for communities
bloc = [ [1 for _ in range(10)] for _ in range(10)]
for i, line_i in enumerate(bloc):
    line_i[i]=0

bloc_2 = [ [1 for _ in range(20)] for _ in range(20)]
for i, line_i in enumerate(bloc_2):
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


# idem for graph_2 with 3 communities
graph_2 = [ [0 for _ in range(50)] for _ in range(50)]

for i in range(20):
    graph_2[i][0:20]=bloc_2[i]
    graph_2[i+20][20:40]=bloc_2[i]

for i in range(10):
        graph_2[i+40][40:50]=bloc[i]

graph_2[1][22] = 1
graph_2[22][1] = 1
graph_2[3][25] = 1
graph_2[25][3] = 1
graph_2[6][28] = 1
graph_2[28][6] = 1
graph_2[14][32] = 1
graph_2[32][14] = 1
graph_2[16][35] = 1
graph_2[35][16] = 1
graph_2[18][38] = 1
graph_2[38][18] = 1
graph_2[22][42] = 1
graph_2[42][22] = 1
graph_2[33][45] = 1
graph_2[45][33] = 1
graph_2[36][48] = 1
graph_2[48][36] = 1






# trivial attributes
attributes = [[0] for _ in range(20)]

# random binary attributes
import random
bin_attributes = [[random.choice(range(2)) for _ in range(2)] 
                    for _ in range(20)]

bin_3d_attributes = [[random.choice(range(2)) for _ in range(3)] 
                        for _ in range(20)]

attributes_2 = [[random.choice(range(2)) for _ in range(3)] 
                        for _ in range(50)]