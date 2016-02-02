# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:41:27 2016

@author: savinien
"""

import math
import numpy as np
import scipy as sp


class Network:
    """class of networks: graphs (non oriented), with attributes, and node degrees"""

    def __init__(self, adj_matrix, node_attributes=None, node_degrees=None):
        """ - adj_matrix : ajacency matrix of the graph, size n * n, symetric
            - nodes_attributes : matrix, size n * n_a, where n_a is the number 
            of attributes, ie lines = vectors representing nodes attributes.
            By default this is an empty list (graph without attributes).
            - nodes_degrees : vector, size n, with nodes degrees.
            By default this is an empty list."""        

        self.matrix = adj_matrix
        if node_attributes is None and node_degrees is None:
            self.node_attributes = []
            self.node_degrees = []
        elif node_attributes is None and node_degrees is not None:
            self.node_attributes = []
            if len(adj_matrix[0]) == len(node_degrees):
                self.node_degrees = node_degrees
            else:
                print("sizes of input elements don't match!")
        elif node_attributes is not None and node_degrees is None:
            self.node_degrees = []
            if len(adj_matrix[0]) == len(node_attributes):
                self.node_attributes = node_attributes
            else:
                print("sizes of input elements don't match!")
        else:
            if len(adj_matrix[0]) == len(node_attributes[0]) and len(adj_matrix[0]) == len(node_degrees):
                self.node_attributes = node_attributes
                self.node_degrees = node_degrees
            else:
                print("sizes of input elements don't match!")


#    def fuse_nodes(self,other_network):
#        if len(self.nodes) == len(other_network.nodes):
#            net= [] + other_network.nodes
#            for i, attribute in enumerate(net):
#                self.nodes[i] += attribute
#            return net
#        else:
#            return print("graph sizes don't match")



def get_graph_degrees(adj_matrix):
    """computes the degrees of nodes in a network (non oriented)
        - input: adj_matrix = ajacency (symetric) matrix of a graph
        - output: vector of nodes degrees (ordered as in adj_matrix)"""
    deg=[]
    for i, line_i in enumerate(adj_matrix):
        deg.append(0)
        for j, link_ij in enumerate(line_i):
            if j != i :             # discard loops !
                deg[i] += link_ij
    return deg



