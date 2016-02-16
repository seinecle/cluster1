# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:41:27 2016

@author: savinien
"""

import math
import numpy as np
import scipy as sp
import copy
from blist import blist
import sym_mat_class

def tot_num_edges(adj_matrix):
    """computes the total number of edges in the graph"""
    # adj_matrix is a sym matrix, class Sym_mat.matrix
    m = sum( sum( coef for _, coef in enumerate(line) ) 
            for _,line in enumerate(adj_matrix) )
    return m

def vect_add(u,v):
    s =  [x + y for x,y in zip(u,v)]
    return s

def list_merge(list_keep,list_remove):
    """ merges the two lists """
    # if both lists are single vectors
    if type(list_keep[0]) is int and type(list_remove[0]) is int:
        l=blist([])
        l.append(list_keep)
        l.append(list_remove)
    # if one list is a single vector and the other a list of vectors
    elif type(list_keep[0]) is int:
        l=blist(list_remove[:])
        l.append(list_keep)
    elif type(list_remove[0]) is int:
        l=blist(list_keep[:])
        l.append(list_remove)
    # if both are lists of vectors
    else:
        if len(list_keep)>= len(list_remove):
            l=blist(list_keep[:])
            for _, attr in enumerate(list_remove):
                l.append(attr)
        else:
            l=blist(list_remove[:])
            for _, attr in enumerate(list_keep):
                l.append(attr)
    return l 


class Network:
    """class of networks: graphs (non oriented), with attributes, and node degrees"""

    def __init__(self, sym_mat = None): #, node_attributes = None):
        """ - sym_mat : ajacency matrix of the graph, symetric, class Sym_mat
            - nodes_attributes : matrix, size n * n_a, where n_a is the number 
            of attributes, ie lines = vectors representing nodes attributes.
            By default this is an empty list (graph without attributes). """        
        if sym_mat is None:
            self.graph = Sym_mat() 
            #self.node_attributes = blist([])
            self.node_degrees = blist([])
            self.tot_num_edges = 0
        else:
            self.graph = sym_mat
            self.node_degrees = get_graph_degrees_sym(sym_mat)
            self.tot_num_edges = tot_num_edges(sym_mat.matrix)
            #if node_attributes is None:
            #    self.node_attributes = blist([])
            #else: 
            #    if len(sym_mat.matrix) == len(node_attributes):
            #        self.node_attributes = blist(node_attributes)
            #    else:
            #        print("sizes of attributes' list and graph matrix don't match!")

   
    def modularity_bare(self, tot_num_edges = None):
        """computes the 'bare' modularity of the graph of communities"""
        if tot_num_edges is None:
            m = self.tot_num_edges
        else:
            m = tot_num_edges
        # self.matrix is a sym matrix, class Sym_mat
        q_1 = sum( line_i[0] for _,line_i in enumerate(self.graph.matrix) )
        q_1 = q_1 / m
        q_2 = sum( d ** 2 for d in self.node_degrees) / 4 / m / m 
        return q_1 - q_2

    def fuse_nodes(self,node_1,node_2): #, method = vect_add):
        """ fuses two nodes, adds their degrees, merges their edges, and
        updates the adjacency matrix, and adds their attributes"""
        node_keep = min(node_1, node_2)
        node_remove = max(node_1, node_2)

        # add up degrees, and update node_degrees
        self.node_degrees[node_keep] += self.node_degrees[node_remove]
        del self.node_degrees[node_remove]
        
        # merge edges and update adjacency matrix
        # - update line #node_keep
        edges_between_nodes_to_fuse = self.graph.coef(node_keep,node_remove)
        loops_on_node_to_remove = self.graph.coef(node_remove,node_remove)
        for k in range( len(self.graph.matrix) ):
            edges = self.graph.coef(node_remove,k)
            if all([edges,  k - node_keep,  k - node_remove]):
                self.graph.add_to_coef(node_keep,k,edges)
        self.graph.add_to_coef(node_keep,node_keep,
                               edges_between_nodes_to_fuse
                               + loops_on_node_to_remove)      
               
        # - delete line #node_remove (and column #node_remove)
        self.graph.delete_line(node_remove)
                
        # add attributes # TO DO: choose a merging function
        #self.node_attributes[node_keep] = method(self.node_attributes[node_keep], 
        #                                        self.node_attributes[node_remove])
        #del self.node_attributes[node_remove]

        return self
        
    def copy(self):
        net = Network()
        net.graph = copy.deepcopy(self.graph)
        #net.node_attributes = copy.deepcopy(self.node_attributes)
        net.node_degrees = copy.deepcopy(self.node_degrees)
        net.tot_num_edges = self.tot_num_edges
        return net
    



def get_graph_degrees(adj_matrix):
    """computes the degrees of nodes in a network (non oriented)
        - input: adj_matrix = ajacency (symetric) matrix of a graph
        - output: vector of nodes degrees (ordered as in adj_matrix)"""
    deg=blist([])
    for i, line_i in enumerate(adj_matrix):
        deg.append(0)
        for j, link_ij in enumerate(line_i):
            if j != i :             # discard loops !
                deg[i] += link_ij
    return deg


def get_graph_degrees_sym(sym_mat):
    """computes the degrees of nodes in a network (non oriented)
        - input: sym_matrix = ajacency symetric matrix (class Sym_mat)
        - output: vector of nodes degrees (ordered as in sym_mat.matrix)"""
    deg=blist([])
    for i, _ in enumerate(sym_mat.matrix):
        deg.append(0)
        deg[i] = sym_mat.sum_line(i)
    return deg


