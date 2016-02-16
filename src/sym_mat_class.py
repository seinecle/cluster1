# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:07:13 2016

@author: savinien
"""

class Sym_mat:
    """ class of symmetric matrices """
    def __init__(self, matrix = None):
        if matrix is None:
            self.matrix = blist([])
        else:
            self.matrix = blist( [ blist(matrix[i][i:]) 
                                    for i,_ in enumerate(matrix) ] )
    
    def coef(self, i, j):
        if i <= j:
            return self.matrix[i][j-i]
        else:
            return self.matrix[j][i-j]
    
    def add_to_coef(self,i,j,value):
        if i <= j:
            self.matrix[i][j-i] += value
        else:
            self.matrix[j][i-j] += value

    def delete_line(self,i):
        """ deletes line i (and column i accordingly) """
        del self.matrix[i]
        for k in range(i):
            del self.matrix[k][i-k]

    def sum_line(self,i):
        """ computes the sum of entries on line i, but the diagonal one """
        s = 0
        for k in range(len(self.matrix[0])):
            s += self.coef(i,k)
        s -= self.coef(i,i)
        return s
    
    def return_line(self,i):
        """ returns the full line #i """

##
#
# would it be faster to implement lower diagonal matrices instead?!
#
##

