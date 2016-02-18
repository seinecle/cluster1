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
from collections import Counter

# initialize network
sym_mat = Sym_mat(graph_5)
att = blist(attributes_5)
network = Network(sym_mat = sym_mat)

# parameter for penalization
alpha_mod = 1.
alpha_ent = 0.00005 #
 
# initialize communities (1 per node)
communities = blist([ blist([i]) for i,_ in enumerate(att)])


iter = len(communities)
m = tot_num_edges(sym_mat.matrix) # could use m as arg for modularity

# initialize entropy and gain
community_entropy = blist([ 0. for i,_ in enumerate(att)])
entropy_after_fuse = 0.
gain_after_fuse = alpha_mod * network.modularity_bare()


for _ in range(iter):
    
    entropy_before_fuse = entropy_after_fuse    
    gain_before_fuse = gain_after_fuse
    delta_gain_old = 0.
    
    # test all pairs of communities for fusion
    for i, comm_i in enumerate(communities):
        for k, comm_j in enumerate(communities[i+1:]):
            j=i+1+k # b/c enumerate(communities[i+1:]) starts at k=0

            delta_entropy = cross_community_entropy(comm_i,comm_j,att,
                                                    similarity_measure=cosine_distance)
            delta_modularity = ( network.graph.coef(i,j) / m 
                                - network.node_degrees[i] 
                                * network.node_degrees[j] / 2 / m / m )
            delta_gain_new = ( alpha_mod * delta_modularity
                                - alpha_ent * delta_entropy )
            
            # keep record of pair with highest gain increase
            if delta_gain_new > delta_gain_old:
                delta_gain_after_fuse = delta_gain_new
                gain_after_fuse = gain_before_fuse + delta_gain_after_fuse
                delta_entropy_after_fuse = delta_entropy
                i_keep = i
                i_remove = j
                delta_gain_old = delta_gain_new
    
    # fuse pairs with highest gain increase
    if gain_after_fuse > gain_before_fuse:
        # update gain and print it with selected pairs
        print("Fused communities", i_keep, "&", i_remove,
              "  Gain increase: ", delta_gain_after_fuse)
                
        # update entropy
        entropy_after_fuse = entropy_before_fuse + delta_entropy_after_fuse
        community_entropy[i_keep] += ( community_entropy[i_remove] 
                                        + delta_entropy_after_fuse )
        del community_entropy[i_remove]

        # fuse selected pairs and update communities
        network.fuse_nodes(i_keep,i_remove)
        communities[i_keep] = communities[i_keep] + communities[i_remove]
        del communities[i_remove]
    
    # if no fusing was performed, terminate
    else:
        break


# print final communities
print()
print("alpha_mod=",alpha_mod, " alpha_ent=", alpha_ent)
print()
print("Total entropy = ", entropy_after_fuse)
print("Final communities are: ")
for i, comm in enumerate(communities):
    comm_att = []
    for j in comm:
        comm_att.append(tuple(att[j]))
    print("Community ", i," :")
    print("- nodes : ", sorted(comm))
    print("- attributes: ", end=' ' )
    for val, vec in zip(Counter(comm_att).values(),Counter(comm_att).keys()):
        print(list(vec), " (",val,")", sep='', end='  ')
    print()
    print("- entropy :", community_entropy[i])
    print()


