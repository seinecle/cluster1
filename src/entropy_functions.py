# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:23:13 2016

@author: savinien
"""

import math
import numpy as np
import scipy as sp


def norm_2(u):
    """ computes the Euclidean norm of vector u """
    return math.sqrt(sum( a**2 for a in u))


def cosine_distance(u,v):
    """ computes the "cosine distance" between two vectors u,v:
        cosine_distance(u,v) = u.v / norm_2(u) / norm_2(v) 
        ie cos(theta) where theta is the angle between u and v """

    dot = sum( a*b for a,b in zip(u,v) ) 
    if dot == 0.:
        return 0.
    elif u == v:
        return 1.
    else:
        return dot / norm_2(u) / norm_2(v)


def attribute_match(u,v):
    """ computes a similarity measure of two vectors of attributes, based on
        attributes' matches (Hamming distance):
        - input: 2 vectors u,v with entries 0 or 1
        - ouput: number of equal coordinates / vector-length, ie a number
        between 0 (no match), and 1 (perfect match)"""
    return sum(1 for a,b in zip(u,v) if a==b)/len(u)
    #if len(u) == len(v):
    #    return sum(1 for a,b in zip(u,v) if a==b)/len(u)
    #else:
    #    print("sizes of input vectors are incompatible")
        

# it looks like the name "entropy" is used by some libraries I'm using...
# so I'm renaming this function "entropie"
def entropie(p):
    """ computes -p * log(p) - (1-p) * log (1-p) """
    if p > 0. and p < 1.:
        q = 1. - p
        return - p*math.log(p) - q * math.log(q)
    elif p > 0.:
        return - p*math.log(p)
    elif p<1.:
        q = 1. - p
        return - q * math.log(q)
    else:
        return 0.

def cross_community_entropy(community_1, community_2, attributes,
                            similarity_measure = attribute_match):
    """ computes the "cross entropy" of attributes in community_1 and 
        attributes in community_2: the sum of entropy(attributes(i_1),
                                                      attributes(i_2)) 
        for i_k in community_k, k=1,2. """
    ent = 0.
    for i_1 in community_1:
        for i_2 in community_2:
            ent += entropie(similarity_measure(attributes[i_1],
                                               attributes[i_2]))
    return ent

