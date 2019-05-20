#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 18:26:22 2019

@author: sbk
"""

class Tree: 

	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def evaluateExpressionTree(root): 
  
    # empty tree 
    if root is None: 
        return 0
  
    # leaf node 
    if root.left is None and root.right is None: 
        return int(root.data) 
  
    # evaluate left tree 
    left_sum = evaluateExpressionTree(root.left) 
  
    # evaluate right tree 
    right_sum = evaluateExpressionTree(root.right) 
  
    # check which operation to apply 
    if root.data == '+': 
        return left_sum + right_sum 
      
    elif root.data == '-': 
        return left_sum - right_sum 
      
    elif root.data == '*': 
        return left_sum * right_sum 
      
    else: 
        return left_sum / right_sum 
    
if __name__=='__main__': 
      
    # creating a sample tree 
    root = Tree('+') 
    root.left = Tree('*') 
    root.left.left = Tree('5') 
    root.left.right = Tree('4') 
    root.right = Tree('-') 
    root.right.left = Tree('100') 
    root.right.right = Tree('20') 
    print(evaluateExpressionTree(root))
