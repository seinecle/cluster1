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


import random

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



# idem for graph_3 with 4 communities
graph_3 = [ [0 for _ in range(70)] for _ in range(70)]

for i in range(20):
    graph_3[i][0:20]=bloc_2[i]
    graph_3[i+20][20:40]=bloc_2[i]
    graph_3[i+50][50:70]=bloc_2[i]

for i in range(10):
        graph_3[i+40][40:50]=bloc[i]

graph_3[1][22] = 1
graph_3[22][1] = 1
graph_3[3][25] = 1
graph_3[25][3] = 1
graph_3[6][28] = 1
graph_3[28][6] = 1
graph_3[14][32] = 1
graph_3[32][14] = 1
graph_3[14][68] = 1
graph_3[68][14] = 1
graph_3[16][35] = 1
graph_3[35][16] = 1
graph_3[18][38] = 1
graph_3[38][18] = 1
graph_3[22][42] = 1
graph_3[42][22] = 1
graph_3[33][45] = 1
graph_3[45][33] = 1
graph_3[36][48] = 1
graph_3[48][36] = 1
graph_3[53][10] = 1
graph_3[10][53] = 1
graph_3[58][22] = 1
graph_3[22][58] = 1
graph_3[63][35] = 1
graph_3[35][63] = 1
graph_3[65][55] = 1
graph_3[55][65] = 1
graph_3[68][21] = 1
graph_3[21][68] = 1

##
#
# random graphs with probable communities (graph_4 has 100 nodes, graph_5 500)
#
##
graph_4 = [ [ 0 for _ in range(100)] for _ in range(100)]

for i in range(100):
    for j in range(100):
        if i<= 50:
            if j<= 50:
                if random.random() <= 0.8:
                    graph_4[i][j] = 1
            else:
                if random.random() <= 0.1:
                    graph_4[i][j] = 1
        if i>50:
            if j>50:
                 if random.random() <= 0.8:
                    graph_4[i][j] = 1
            else:
                if random.random()<= 0.1:
                    graph_4[i][j] = 1
    if graph_4[i][i] == 1:
        graph_4[i][i] = 0


graph_5 = [ [ 0 for _ in range(500)] for _ in range(500) ]
for i in range(500):
    for j in range(500):
        if i<= 100:
            if j<= 100:
                if random.random() <= 0.8:
                    graph_5[i][j] = 1
            else:
                if random.random() <= 0.1:
                    graph_5[i][j] = 1
        if i>100 and i<=200:
            if j>100 and j<=200:
                 if random.random() <= 0.8:
                    graph_5[i][j] = 1
            else:
                if random.random()<= 0.1:
                    graph_5[i][j] = 1
        if i>200 and i<=300:
            if j>200 and j<=300:
                 if random.random() <= 0.8:
                    graph_5[i][j] = 1
            else:
                if random.random()<= 0.1:
                    graph_5[i][j] = 1
        if i>300 and i<=400:
            if j>300 and j<=400:
                 if random.random() <= 0.8:
                    graph_5[i][j] = 1
            else:
                if random.random()<= 0.1:
                    graph_5[i][j] = 1
        if i>400:
            if j>400:
                 if random.random() <= 0.8:
                    graph_5[i][j] = 1
            else:
                if random.random()<= 0.1:
                    graph_5[i][j] = 1 
    if graph_5[i][i] == 1:
        graph_5[i][i] = 0






# trivial attributes
attributes = [[0] for _ in range(20)]

# random binary attributes
bin_attributes = [[random.choice(range(2)) for _ in range(2)] 
                    for _ in range(20)]

bin_3d_attributes = [[random.choice(range(2)) for _ in range(3)] 
                        for _ in range(20)]

attributes_2 = [[random.choice(range(2)) for _ in range(3)] 
                        for _ in range(50)]

attributes_3 = [[random.choice(range(2)) for _ in range(3)] 
                        for _ in range(70)]

attributes_4 = [[random.choice(range(2)) for _ in range(3)] 
                        for _ in range(100)]

attributes_5 = [[random.choice(range(2)) for _ in range(3)] 
                        for _ in range(500)]
