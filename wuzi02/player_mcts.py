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
import random

class MCTS_SATE(Enum):
    Selection = 1
    Expansion = 2
    Simulation = 3
    Backpropagation =4



'''
#mcts 棋手
#输出：
1.创建
2.获取已落子
3.落子（play ） 下一步        输入：game
4.读取经验文件  loadTreeFile
5.保存经验文件  saveTreeFile
 // 6.落子（走棋action ）  返回：棋面，是否结束，赢棋  self.RunAction,  isOver, isWin
7.训练(trainPlay)  训练n轮 输入:game, player_random, nRound

内部函数：
1. 落子选择  ： 1）随机  2）训练选择  3）比赛选择
2. BP反馈
3. trainRound 下一局
4. choiceActions_random
5. choiceActions_train
6. choiceActions_real

'''
class GamePlayer_mcts(object):


    ############### 输出函数
    def __init__(self, potColor ):

        self.actionHis = []
        self.color = potColor
        self.name = 'mcts_player'
        self.rootNode = None
        self.curNode  = Node

    def reset(self):
        self.actionHis = []
        pass

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
    def train(self, game, player , nRount ):
        for i in range(nRount):
            gameinfo, isOver, isWin = self.trainRound(game ,player )
            print gameinfo, isOver, isWin
            self.bp();
            player.reset()
            game.reset()
            self.reset()

    ############### 内部函数
    def trainStep(self, game):
        actions = game.getActions()
        action = self.choiceActions(actions)
        self.actionHis = self.actionHis + [action]

        gameInfo, isOver, isWin = game.action(action, self.color)
        return gameInfo, isOver, isWin

    def trainRound(self, game ,player ):
        play1 = player
        play2 = self

        if(random.random() >0.5  ):
            gameinfo, isOver, isWin = play2.trainStep(game)

        while (True):
            gameinfo, isOver, isWin = play1.play(game)
            if (isWin):
                print  play1.name, 'I am win ', play1.color
                return True, game, play1.color
            if (isOver):
                break

            gameinfo, isOver, isWin = play2.trainStep(game)
            if (isWin):
                print play2.name, 'I am win ', play2.color
                return True, game, play2.color
            if (isOver):
                break
            #print game
            pass
        pass
        print 'no win '
        return False, game, 0

    #精华部分
    def choiceActions(self, actions):
        if( self.isExpand ):
            return self.choiceActions_random(actions)
        if( self.isReal ):
            return self.choiceActions_real(actions)
        if( self.isTrain ):
            return self.choiceActions_train(actions)

        #throw 'error'
        print ' error '
        return random.choice(actions)

    #
    def choiceActions_random(self, actions):
        action = random.choice(actions)
        return action

    #获取当前节点， 遍历子节点，选取 UCB 值最大的
    def choiceActions_real(self, actions):
        action = random.choice(actions)
        return action

    #优先选择 未走过的路径， 进入路径后，开始展页模式  如果所有路径走过之后， 选择UCB最大的
    def choiceActions_train(self, actions):
        action = random.choice(actions)
        return action

    #获取当前节点，向上溯源，回馈计算
    def bp(self):
        pass


    def __repr__(self):
        return "color: {}, actionHis: {},  ".format(self.color, self.actionHis)