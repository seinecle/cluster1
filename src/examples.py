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
net_1=Network(adj_matrix)
net_1.node_attributes = node_att
net_1.node_degrees = deg
print(net_1.matrix, net_1.node_attributes, net_1.node_degrees)

# constructor with some arguments
net_2=Network(adj_matrix,node_attributes=node_att)
net_2.node_degrees = deg
print(net_2.matrix, net_2.node_attributes, net_2.node_degrees)

net_3=Network(adj_matrix,node_degrees = deg)
net_3.node_attributes = node_att
print(net_3.matrix, net_3.node_attributes, net_3.node_degrees)



