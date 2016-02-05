# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:23:13 2016

@author: savinien
"""

import math
import numpy as np
import scipy as sp


def attribute_match(u,v):
    """ computes a similarity measure of two vectors of attributes, based on
        attributes' matches (Hamming distance):
        - input: 2 vectors u,v with entries 0 or 1
        - ouput: number of equal coordinates / vector-length, ie a number
        between 0 (no match), and 1 (perfect match)"""
    if len(u) == len(v):
        return sum(1 for a,b in zip(u,v) if a==b)/len(u)
    else:
        print("sizes of input vectors are incompatible")
        

def cluster_match(cluster_attributes):
    """ computes a measure of attributes's matchings:
        - input: list [u_0,... u_(k-1)] of vectors of the cluster's attributes
        - output: sum of attribute_match(u_i,u_j) (pairwise distinct)"""
    if len(cluster_attributes) == 1:
        return 0. # if cluster is a single node, matching = 0
    else:
        match = 0.
        for i, u_i in enumerate(cluster_attributes):
            for j, u_j in enumerate(cluster_attributes[i+1:]):
               match += attribute_match(u_i,u_j)
        return match


def entropy(p):
    """ computes -p * log(p) - (1-p) * log (1-p) """
    if p > 0 and p < 1:
        q = 1 - p
        return - p*math.log(p) - q * math.log(q)
    elif p > 0:
        return - p*math.log(p)
    elif p<1:
        q = 1 - p
        return - q * math.log(q)
    else:
        return 0.


def cluster_entropy(cluster_attributes, similarity_measure = attribute_match):
    """ computes the entropy of a cluster's attributes, according to a similarity
        measure to specify:
        - input: - list [u_0,... u_(k-1)] of vectors of the cluster's attributes
                 - similarity measure (default = attribute_match)
        - output: sum of entropy(similarity_measure(u_i,u_j)) (pairwise distinct)"""
    if len(cluster_attributes) == 1:
        return 0. # if cluster is a single node, entropy = 0
    else:
        ent = 0.
        for i, u_i in enumerate(cluster_attributes):
            for j, u_j in enumerate(cluster_attributes[i+1:]):
               ent += entropy(similarity_measure(u_i,u_j))
        return ent


