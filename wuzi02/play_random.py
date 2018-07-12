#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import random


class GamePlayer(object):

    def __init__(self, potColor ):
        self.actionHis = []
        self.color = potColor
        self.name = 'random_player'

    def reset(self):
        self.actionHis = []

    def getActionHis(self):
        return self.actionHis

    #游戏
    def play(self, game):
        actions = game.getActions()
        action = self.choiceActions( actions )
        self.actionHis = self.actionHis +[action]

        gameInfo, isOver, isWin = game.action(action, self.color)

        return gameInfo, isOver, isWin




    def choiceActions(self, actions):
        action = random.choice(actions)
        return action

    def __repr__(self):
        return "color: {}, actionHis: {},  ".format(self.color, self.actionHis)


