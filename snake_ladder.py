#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:29:49 2020

@author: hitesh
"""
import numpy as np
import random as rnd
from matplotlib import pyplot as plt

class board:
    
    def __init__ (self):
        """
        Initialise board to empty dictionary
        """
        self.graph = {}
        
    def line_init (self,N):
        """
        Make straight graph with no snakes and ladders
        """
        self.graph = { x:[n for n in [y for y in range(x+1,x+7)] if n <= N] \
                                      for x in range(1,N) }
        
        
    def snake_ladder (self,a,b):
        """
        Add snake or ladder from a to b to the graph
        """
        nodes = range(a-6,a) 
        nodes = [ n for n in nodes if n > 0]
        for i in nodes:
            self.graph[i][a-i-1] = b
            
    def play (self):
        """
        To play one game of snakes and ladder
        Returns number of dice rolls
        """
        mark = 1
        dice = [1,2,3,4,5,6]
#        mark_list = []
#        count_list = []
        count = 0
        N = list(self.graph.keys())[-1] + 1
        while mark!=N:
            roll = rnd.choice(dice)
            if roll <= N-mark:
                mark = self.graph[mark][roll-1]
            count +=1
#            mark_list.append(mark)
#            count_list.append(count)
        
#        plt.figure()
#        plt.plot(count_list,mark_list)
        return count
        
        
a = board()
a.line_init(100)

# Ladders
a.snake_ladder(8,26)
a.snake_ladder(19,38)
a.snake_ladder(36,57)
#a.snake_ladder(40,82)
#a.snake_ladder(43,77)
#a.snake_ladder(50,91)
#a.snake_ladder(54,88)
#a.snake_ladder(61,99)
#a.snake_ladder(63,97)
#a.snake_ladder(66,87)
#a.snake_ladder(23,60)

# Snakes
a.snake_ladder(34,7)
a.snake_ladder(52,11)
a.snake_ladder(59,18)
a.snake_ladder(64,24)
a.snake_ladder(68,2)
a.snake_ladder(69,33)
a.snake_ladder(80,62)
a.snake_ladder(83,22)
a.snake_ladder(89,51)
a.snake_ladder(93,67)
a.snake_ladder(98,13)


################Plot mark

count_list = []
exp_no = 500000
print_skip = int(exp_no/10)

print('\nRunning experiments',end=' ')
for t in range(exp_no):
    count_list.append(a.play())
    if t%print_skip==0:
        print('.',end='')
print('\n')


plt.figure(figsize=(8,8))
binwidth = 1
his = plt.hist(count_list,bins=range(min(count_list), max(count_list) + binwidth, binwidth))
#print('Average number of rolls      : ',sum(count_list)/exp_no)
print('Most probable number of rolls: ',his[1][np.argmax(his[0])])

#count = a.play()
#print(count)
    