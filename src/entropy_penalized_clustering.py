# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:37:34 2016

@author: savinien
"""

import math
import numpy as np
import scipy as sp

import graph_build
import network_class
import entropy_functions


# initialize network
initial_graph = copy.deepcopy(graph_2)
network = Network(initial_graph)
#network.node_attributes = copy.deepcopy(bin_attributes)
network.node_attributes = copy.deepcopy(attributes_2)

# parameter for penalization
alpha_mod = 1.
alpha_ent = 0.003

# initialize communities (1 per node)
communities = [ [i] for i,_ in enumerate(initial_graph)]

iter = len(communities)

for _ in range(iter):
    
    gain_before_fuse = (alpha_mod * network.modularity_bare()
                        - alpha_ent * total_entropy(network.node_attributes))
    gain_after_fuse = gain_before_fuse
    gain_old = gain_before_fuse
    
    # test all pairs of nodes for fusion
    for i, _ in enumerate(communities):
        for j in range(i+1,len(communities)):
            net = network.copy()
            net.fuse_nodes(i,j, method= list_merge)
            gain_new = (alpha_mod * net.modularity_bare() 
                        - alpha_ent * total_entropy(net.node_attributes))

            # keep record of pair with highest modularity increase
            if gain_new > gain_old:
                gain_after_fuse = gain_new
                i_keep = i
                i_remove = j
                gain_old = gain_after_fuse
    
    # fuse pairs with highest modularity increase
    if gain_after_fuse > gain_before_fuse:
        print("new gain after fuse: ", gain_after_fuse)
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
    print("Community ", i," :")
    print("- nodes : ", sorted(comm))
    print("- attributes : ", sorted(network.node_attributes[i]))
    print("- entropy :", cluster_entropy(network.node_attributes[i]))
    print()


