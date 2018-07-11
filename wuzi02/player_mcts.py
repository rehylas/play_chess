#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:hylas

'''

MCTS  四个阶段：
1.Selection
就是在树中找到一个最好的值得探索的节点，一般策略是先选择未被探索的子节点，如果都探索过就选择UCB值最大的子节点。

2.Expansion
就是在前面选中的子节点中走一步创建一个新的子节点，一般策略是随机自行一个操作并且这个操作不能与前面的子节点重复。

3.Simulation
就是在前面新Expansion出来的节点开始模拟游戏，直到到达游戏结束状态，这样可以收到到这个expansion出来的节点的得分是多少

4.Backpropagation
就是把前面expansion出来的节点得分反馈到前面所有父节点中，更新这些节点的quality value和visit times，方便后面计算UCB值

'''

from enum import Enum

class MCTS_SATE(Enum):
    Selection = 1
    Expansion = 2
    Simulation = 3
    Backpropagation =4

class Node():
    def __init__(self ):
        self.data = [ 0,0, () ]   #times, wins, values
        self.nodeInfo=[ 0, 0, 0 ]   #type 0 root, 1 node, 2 leves ;   sons, level

        #self.times = 0
        #self.wins = 0
        #self.values = ()
        self.parent = None
        self.children = []
        pass

    def getType(self):
        return self.nodeInfo[0]

    def setVaule(self, value):
        self.data[2] = value

    def setParent(self, parentNode):
        self.parent = parentNode

    def addChild(self, childNode ):
        self.children += [ childNode ]


    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        return False

class Tree():
    def __init__(self):
        pass

    def load(self, filename ):
        pass

    def save(self, filename):
        pass

    def expandNode(self, parentNode, value ):
        childNode = Node()
        childNode.setVaule( value )
        childNode.setParent( parentNode )
        parentNode.addChild( childNode )
        return  childNode

        pass



class GamePlayer(object):

    def __init__(self, potColor ):

        self.actionHis = []
        self.color = potColor


    def getActionHis(self):
        return self.actionHis

    #游戏
    def play(self, game):
        actions = game.getActions()
        action = self.choiceActions( actions )
        self.actionHis = self.actionHis +[action]

        gameInfo, isOver, isWin = game.action(action, self.color)

        return gameInfo, isOver, isWin

    #训练
    def train(self, game):
        actions = game.getActions()
        action = self.choiceActions(actions)
        self.actionHis = self.actionHis + [action]

        gameInfo, isOver, isWin = game.action(action, self.color)

        return gameInfo, isOver, isWin


    def choiceActions(self, actions):
        action = random.choice(actions)
        return action

    def __repr__(self):
        return "color: {}, actionHis: {},  ".format(self.color, self.actionHis)