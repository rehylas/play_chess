#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: hylas zhang

import numpy as np;
import random
import math

from Tree  import *


'''
TreeMcts
输出：


内部：


'''

class TreeMcts(Tree) :

    def __init__(self):
        super( TreeMcts , self).__init__(   )
        self.wins = 0
        self.times = 0
        pass

    def bp(self, isWin):

        while( self.cur_Node.getInfo()[0] != 0 ):
            self.cur_Node.data[1] += 1
            if( isWin ):
                self.cur_Node.data[0] += 1

            self.moveUp()


        pass
        if (isWin):
            self.wins += 1
        self.times += 1


    def getHasActions(self):
        node = self.getCurNode()
        Actions = []
        for child in node.children:
            action = [ (Node.data[2] , Node.data[3]) ]
            Actions += action
        return Actions
        pass

    def getBestUCBAction(self,  avalActions =  None, is_exploration = True ):
        ucbVal = 0.0
        temNode = None
        is_exploration = True

        for node in self.cur_Node :
            if( inList( avalActions) == False ):
                continue

            tempNodeUcbVal = self.getNodeUCB(node, is_exploration )
            if( tempNodeUcbVal > ucbVal  ):
                ucbVal = tempNodeUcbVal
                temNode = node
        return ( temNode.data[2], temNode[3]  )
        pass

    # 内部函數

    #计算 ucbVal
    def getNodeUCB(self, node, is_exploration ):
        quality = node.data[0]
        times = node.data[1]
        total_times = self.times
        ucbVal = ucb( is_exploration, quality, times,  total_times )
        return ucbVal
        pass


def ucb(is_exploration, quality, times, total_times):
    if is_exploration:
        c = 1 / math.sqrt(2.0)
    else:
        c = 0.0

    # ucb = quality /times + c* sqrt(2*ln(total_times) /times)
    # quality = subnode.get_quality_value()
    # times = subnode.get_visit_times()
    # total_times = node.get_visit_times       ( rootnode.get_visit_times  )
    left = quality / times
    right = 2.0 * math.log(total_times / times)
    score = left + c * math.sqrt(right)
    return score

def inList( rec, lst ):
    if rec in lst:
        return True
    else:
        return False

class Person(object):
     def __init__(self, name, gender):
         self.name = name
         self.gender = gender

class Teacher(Person):
     def __init__(self, name, gender, couse):
         super(Teacher, self).__init__(name, gender)
         self.course = couse

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course