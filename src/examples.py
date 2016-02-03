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

adj_matrix = [[1, 2, 1, 1], [2, 3, 2, 1], [1, 2, 1, 5], [1, 1, 5, 0]]
node_att=[[1,0],[1,1],[0,1],[0,0]]
deg=get_graph_degrees(adj_matrix)

# default constructor
net_1 = Network(adj_matrix)
net_1.node_attributes = node_att
net_1.node_degrees = deg
print(net_1.matrix, net_1.node_attributes, net_1.node_degrees)

# constructor with some arguments
import copy
adj_mat = copy.deepcopy(adj_matrix) # indep copy
net_2 = Network(adj_mat,node_attributes=node_att.copy())
net_2.node_degrees = deg.copy()
print(net_2.matrix, net_2.node_attributes, net_2.node_degrees)

net_3 = Network(adj_mat,node_degrees = deg.copy())
net_3.node_attributes = node_att.copy()
print(net_3.matrix, net_3.node_attributes, net_3.node_degrees)

# constructor with all arguments
net_4 = Network(adj_mat, node_attributes = node_att.copy(), node_degrees = deg.copy())
print(net_4.matrix, net_4.node_attributes, net_4.node_degrees)


# test modularity_bare
print("total number of edges of initial network = ", net_1.tot_num_edges())
print("bare moduularity of initial network = ", net_1.modularity_bare())


# test fuse_node
print()
print("fuse nodes 0 and 2")
net_2.fuse_nodes(0,2)

# this shouldn't change
print("total number of edges of fused network = ", net_2.tot_num_edges())

# this should be changing
print("bare modularity of fused network = ", net_2.modularity_bare())

# comparision of initial and fused network
print("initial matrix = ", net_1.matrix, " vs fused matrix = ", net_2.matrix)
print("initial degrees = ", net_1.node_degrees, " vs fused degrees = ", net_2.node_degrees)
print("initial attributes = ", net_1.node_attributes, " vs fused attributes = ", net_2.node_attributes)





##
#
# testing entropy
#
##

import entropy
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






