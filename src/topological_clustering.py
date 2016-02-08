# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:40:50 2016

@author: savinien
"""

import math
import numpy as np
import scipy as sp

import graph_build
import network_class


# initialize network
initial_graph = copy.deepcopy(graph)
network = Network(initial_graph)
network.node_attributes = copy.deepcopy(bin_attributes)


# initialize communities (1 per node)
communities = [ [i] for i,_ in enumerate(initial_graph)]

iter = len(communities)

for _ in range(iter):
    
    gain_before_fuse = network.modularity_bare()
    gain_after_fuse = gain_before_fuse    
    gain_old = gain_before_fuse
    
    # test all pairs of nodes for fusion
    for i, _ in enumerate(communities):
        for j in range(i+1,len(communities)):
            net = network.copy()
            net.fuse_nodes(i,j, method= list_merge)
            gain_new = net.modularity_bare()

            # keep record of pair with highest modularity increase
            if gain_new > gain_old:
                gain_after_fuse = gain_new
                i_keep = i
                i_remove = j
                gain_old = gain_after_fuse
    
    # fuse pairs with highest modularity increase
    if gain_after_fuse > gain_before_fuse:
        print("new gain after fusing 2 nodes is: ", gain_after_fuse)
        network.fuse_nodes(i_keep,i_remove, method= list_merge)
        communities[i_keep] = list_merge(communities[i_keep],communities[i_remove])
        del communities[i_remove]
    # if no fusing was performed, terminate
    else:
        break

# print final communities
print()
print("Final communities are: ")
for i, comm in enumerate(communities):
    print("community ", i," :")
    print("Nodes: ", sorted(comm))
    print("Attributes: ", sorted(network.node_attributes[i]))
    print()




 
    



