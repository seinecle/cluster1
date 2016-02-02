# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:31:16 2016

@author: savinien
"""

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
print(net_1.tot_num_edges())
print(net_1.modularity_bare())


# test fuse_node
print("fuse nodes 0 and 2")
net_2.fuse_nodes(0,2)

print("initial degrees = ", net_1.node_degrees, "fused degrees = ", net_2.node_degrees)
print("initial matrix = ", net_1.matrix, "fused matrix = ", net_2.matrix)
