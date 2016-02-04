# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:41:27 2016

@author: savinien
"""

import math
import numpy as np
import scipy as sp


def tot_num_edges(adj_matrix):
    """computes the total number of edges in the graph"""
    m = 0
    for i, line_i in enumerate(adj_matrix):
        m += sum(nb_edges for j,nb_edges in enumerate(line_i) if j>=i)
    return m

def vect_add(u,v):
    s =  [x + y for x,y in zip(u,v)]
    return s

def list_merge(list_keep,list_remove):
    """ merges the two lists """
    l=[]
    # if both lists are single vectors
    if type(list_keep[0]) is int and type(list_remove[0]) is int:
        l.append(list_keep)
        l.append(list_remove)
    # if one list is a single vector and the other a list of vectors
    elif type(list_keep[0]) is int and type(list_remove[0]) is list:
        l=list_remove[:]
        l.append(list_keep)
    elif type(list_keep[0]) is list and type(list_remove[0]) is int:
        l=list_keep[:]
        l.append(list_remove)
    # if both are lists of vectors
    else:
        l=list_keep[:]
        for _, attr in enumerate(list_remove):
            l.append(attr)
    return l   


class Network:
    """class of networks: graphs (non oriented), with attributes, and node degrees"""

    def __init__(self, adj_matrix, node_attributes=None):
        """ - adj_matrix : ajacency matrix of the graph, size n * n, symetric
            - nodes_attributes : matrix, size n * n_a, where n_a is the number 
            of attributes, ie lines = vectors representing nodes attributes.
            By default this is an empty list (graph without attributes). """        

        self.matrix = adj_matrix
        self.node_degrees = get_graph_degrees(adj_matrix)
        if node_attributes is None:
            self.node_attributes = []
        else: 
            if len(adj_matrix) == len(node_attributes):
                self.node_attributes = node_attributes
            else:
                print("sizes of attributes' list and graph matrix don't match!")

   
    def modularity_bare(self):
        """computes the 'bare' modularity of the graph of communities"""
        m = tot_num_edges(self.matrix)
        q_1 = 0.
        for i, line_i in enumerate(self.matrix):
            q_1 += line_i[i]
        q_1 = q_1 / m
        q_2 = sum( d ** 2 for d in self.node_degrees) / 4 / m / m 
        return q_1 - q_2

    def fuse_nodes(self,node_1,node_2, method = vect_add):
        """ fuses two nodes, adds their degrees, merges their edges, and
        updates the adjacency matrix, and adds their attributes"""
        node_keep = min(node_1, node_2)
        node_remove = max(node_1, node_2)

        # add degrees
        self.node_degrees[node_keep] += self.node_degrees[node_remove]
        del self.node_degrees[node_remove]
        
        # merge edges and update adjacency matrix
        # - update line #node_keep
        edges_between_nodes_to_fuse = self.matrix[node_keep][node_remove]
        loops_on_node_to_remove = self.matrix[node_remove][node_remove]
        for k, edges in enumerate(self.matrix[node_remove]):
            if k != node_keep and k != node_remove:
                self.matrix[node_keep][k] += edges
        self.matrix[node_keep][node_keep] += edges_between_nodes_to_fuse + loops_on_node_to_remove
      
        # - copy line #node_keep into column #node_keep (symetric matrix!)
        for k, edges in enumerate(self.matrix[node_keep]):
            self.matrix[k][node_keep] = edges
        
        # - delete line #node_remove
        del self.matrix[node_remove]
        
        # - delete column #node_remove
        for i , _ in enumerate(self.matrix):
            del self.matrix[i][node_remove]
        
        # add attributes # TO DO: choose a merging function
        self.node_attributes[node_keep] = method(self.node_attributes[node_keep], self.node_attributes[node_remove])
        del self.node_attributes[node_remove]

        return self
        




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




