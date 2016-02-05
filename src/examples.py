# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:31:16 2016
@author: savinien
"""


##
#
# testing network_class
#
##

import network_class
import copy

adj_matrix = [[1, 2, 1, 1], [2, 3, 2, 1], [1, 2, 1, 5], [1, 1, 5, 0]]
node_att=[[1,0],[1,1],[0,1],[0,0]]
deg=get_graph_degrees(adj_matrix)

# default constructor
net_0 = Network()
net_0.matrix = adj_matrix
net_0.node_degrees = deg
net_0.node_attributes = node_att
print("net_0: ",net_0.matrix, net_0.node_attributes, net_0.node_degrees)
net = net_0.copy()
print("net_0.copy() :",net.matrix, net.node_attributes, net.node_degrees)

# constructor with attributes
net_1 = Network(adj_matrix)
net_1.node_attributes = node_att
print(net_1.node_degrees == deg)
print(net_1.matrix, net_1.node_attributes, net_1.node_degrees)

adj_mat = copy.deepcopy(adj_matrix) # indep copy
node_att_2 = copy.deepcopy(node_att)
net_2 = Network(adj_mat, node_attributes = node_att_2)
print(net_2.matrix, net_2.node_attributes, net_2.node_degrees)


# test modularity_bare
print("total number of edges of initial network = ", tot_num_edges(net_1.matrix))
print("bare modularity of initial network = ", net_1.modularity_bare())


# test fuse_node
print()
print("fuse nodes 0 and 2, with vector add of attributes")
net_2.fuse_nodes(0,2)

# this shouldn't change
print("total number of edges of fused network = ", tot_num_edges(net_2.matrix))

# this should be changing
print("bare modularity of fused network = ", net_2.modularity_bare())

# comparision of initial and fused network
print("initial matrix = ", net_1.matrix, " vs fused matrix = ", net_2.matrix)
print("initial degrees = ", net_1.node_degrees, " vs fused degrees = ", net_2.node_degrees)
print("initial attributes = ", net_1.node_attributes, " vs fused attributes = ", net_2.node_attributes)

print()
print("fuse nodes 0 and 2, with merging of attributes")
net_0.fuse_nodes(0,2, method = list_merge)

# this shouldn't change
print("total number of edges of fused network = ", tot_num_edges(net_0.matrix))

# this should be changing
print("bare modularity of fused network = ", net_0.modularity_bare())

# comparision of initial and fused network
print("initial matrix = ", net_1.matrix, " vs fused matrix = ", net_0.matrix)
print("initial degrees = ", net_1.node_degrees, " vs fused degrees = ", net_0.node_degrees)
print("initial attributes = ", net_1.node_attributes, " vs fused attributes = ", net_0.node_attributes)






##
#
# testing entropy
#
##

import entropy_functions
from matplotlib import pyplot as plt

xs = [x / 100 for x in range(101)]
plt.plot(xs,[entropy(x) for x in xs],'r-')
plt.axis([0,1,0,.8])
plt.title("entropy(x) = - x*log(x) - (1-x)*log(1-x)")
plt.show()


print("testing entropy")
u=[1,0,0,0]
v=[0,1,0,0]
w=[0,0,1,0]
x=[0,0,0,1]

print("cluster entropy =", cluster_entropy([u,v,w,x]), 
      " cluster match = ", cluster_match([u,v,w,x]))
for i in range(3):
    x[i]=1
    print("cluster entropy =", cluster_entropy([u,v,w,x]), 
          " cluster match = ", cluster_match([u,v,w,x]))
