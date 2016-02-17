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
    """computes the total number of edges in the graph
        inpute: adj_matrix is a sym matrix, class Sym_mat.matrix """
    m = sum( sum( coef for _, coef in enumerate(line) ) 
            for _,line in enumerate(adj_matrix) )
    return m

def get_graph_degrees_sym(sym_mat):
    """computes the degrees of nodes in a network (non oriented)
        - input: sym_matrix = ajacency symetric matrix (class Sym_mat)
        - output: vector of nodes degrees (ordered as in sym_mat.matrix)"""
    deg=blist([])
    for i, _ in enumerate(sym_mat.matrix):
        deg.append(0)
        deg[i] = sym_mat.sum_line(i)
    return deg

class Network:
    """class of networks: graphs (non oriented), with attributes, and node degrees"""

    def __init__(self, sym_mat = None):
        """ input: sym_mat = ajacency matrix of the graph, symetric, 
            of the class Sym_mat """        
        if sym_mat is None:
            self.graph = Sym_mat() 
            self.node_degrees = blist([])
            self.tot_num_edges = 0
        else:
            self.graph = sym_mat
            self.node_degrees = get_graph_degrees_sym(sym_mat)
            self.tot_num_edges = tot_num_edges(sym_mat.matrix)
   
    def modularity_bare(self, tot_num_edges = None):
        """computes the 'bare' modularity of the graph of communities"""
        if tot_num_edges is None:
            m = self.tot_num_edges
        else:
            m = tot_num_edges
        # self.matrix is a sym matrix, class Sym_mat: 
        # diagonal entry on line_i is line_i[0]
        q_1 = sum( line_i[0] for _,line_i in enumerate(self.graph.matrix) )
        q_1 = q_1 / m
        q_2 = sum( d ** 2 for d in self.node_degrees) / 4 / m / m 
        return q_1 - q_2

    def fuse_nodes(self,node_1,node_2):
        """ fuses two nodes, adds their degrees, merges their edges, and
        updates the adjacency matrix """
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
        
        return self
        
    def copy(self):
        net = Network()
        net.graph = copy.deepcopy(self.graph)
        net.node_degrees = copy.deepcopy(self.node_degrees)
        net.tot_num_edges = self.tot_num_edges
        return net
    





