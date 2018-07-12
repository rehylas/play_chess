#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import random
import numpy as np

from wuziboard import WuziBoard,PotColor

from enum import Enum
from play_random import  GamePlayer

ROW_NUM = 10
ECO_NUM = 10
'''
#五子棋游戏
#输出：
1.创建
2.复位
3.获取可落子清单
4.获取盘面状态
5.是否结束
6.落子（走棋action ）  返回：棋面，是否结束，赢棋  self.RunAction,  isOver, isWin

'''

class GameFivePot(object):

	def __init__(self):
		self.potCount  =0;
		self.AllAction	=[]
		self.ActionHis = []

		for x in range(ROW_NUM):
				for y in range(ECO_NUM):
					self.AllAction	 += [(x,y)]

		self.AvailAction = self.AllAction
		self.RunAction = [[0 for col in range(ROW_NUM)] for row in range(ECO_NUM)]

  	def reset(self):
		self.__init__(self)
		pass

	def getActions(self):
		return self.AvailAction
		
	def getRunAction(self):  	
		return self.RunAction

 	def getActionHis(self):
		return  self.ActionHis
 
	def is_over(self, action, potColor):
		x = action[0]
		y = action[1]
		dimCount =[1,1,1,1]
		
		#���� xiang qian
		for x1 in range(x+1, x+5):

			if(x1 >= ROW_NUM ):
				break
			if( self.RunAction[x1][y] == potColor ):
				dimCount[0] +=1 
			else:
				break
				
		#- xiang hou
		for x1 in range(x-1, x-5, -1 ):
			if(x1 < 0 ):
				break
				
			if( self.RunAction[x1][y] == potColor ):
				dimCount[0] +=1 
			else:
				break
				
		if( dimCount[0] >= 5 ):
			return True,True
			
		#���� ����
		for y1 in range(y+1, y+5):
			if(y1 >= ROW_NUM ):
				break
				
			if( self.RunAction[x][y1] == potColor ):
				dimCount[1] +=1 
			else:
				break
				
		#- ����
		for y1 in range(y-1, y-5, -1 ):
			if(y1 < 0 ):
				break
				
			if( self.RunAction[x][y1] == potColor ):
				dimCount[1] +=1 
			else:
				break
				
		if( dimCount[1] >= 5 ):
			return True,True
							
		#-��б ����
		for offset in range(1 ,5):
			x1 = x+offset
			y1 = y+offset
			
			if(y1 >= ROW_NUM or x1 >= ROW_NUM  ):
				break
				
			if( self.RunAction[x1][y1] == potColor ):
				dimCount[2] +=1 
			else:
				break
				
		#- ����
		for offset in range(-1, -5, -1 ):
			x1 = x+offset
			y1 = y+offset			
			if(y1 < 0 or x1<0):
				break
				
			if( self.RunAction[x1][y1] == potColor ):
				dimCount[2] +=1 
			else:
				break
				
		if( dimCount[2] >= 5 ):
			return True,True
				
		#-��б ���� 
		for offset in range(1 ,5):
			x1 = x+offset
			y1 = y-offset
			
			if(y1 < 0 or x1 >= ROW_NUM  ):
				break
				
			if( self.RunAction[x1][y1] == potColor ):
				dimCount[3] +=1 
			else:
				break
				
		#- ���� 
		for offset in range(-1, -5, -1 ):
			x1 = x+offset
			y1 = y-offset			
			if(y1 >= ROW_NUM  or x1<0 ):
				break
				
			if( self.RunAction[x1][y1] == potColor ):
				dimCount[3] +=1 
			else:
				break
				
		if( dimCount[3] >= 5 ):
			return True,True
			
		if( len(self.AvailAction) == 0 ):
			return True,False
		
		return False,False
		pass   
			
			
	def action( self, action,potColor ):
		self.potCount +=1
		self.ActionHis += [  ( action[0], action[1], potColor )  ]
		self.AllAction.remove(  action  )

		self.RunAction[ action[0] ][  action[1] ] =potColor

		isOver, isWin = self.is_over(action, potColor)
		return self.RunAction,  isOver, isWin

	def __repr__(self):
		return "Game step count: {}, AvailAction len: {},  ".format( self.potCount,	 len(self.AvailAction) )
		


def playRount():

	play1 = GamePlayer(PotColor.Black)
	play2 = GamePlayer(PotColor.White)
	game = GameFivePot()

	while (True):
		gameinfo, isOver,isWin = play1.play(game)
		if( isWin):
			print 'I am win ',play1.color
			return True, game,play1.color
		if (isOver):
			break

		gameinfo, isOver,isWin = play2.play(game)
		if( isWin):
			print 'I am win ',play2.color
			return True, game,play2.color
		if (isOver):
			break
		print game
		pass
	pass
	print 'no win '
	return False, game, 0

	pass

def main():
	result, game, winner = playRount()
	actionHis = game.getActionHis()
	drawBoard(ROW_NUM,  actionHis  )
	return

	while( True ):
		result, game, winner = playRount()
		actionHis = game.getActionHis()
		drawBoard(ROW_NUM, actionHis)

		if (result == True ):
			return

def drawBoard(max_count, action_his):
    ActionHis = action_his      #[ (0,1,1), (1,1,2), (5,1,1)   ]
    wuziBoard = WuziBoard( ROW_NUM )
    wuziBoard.drawBoard( ActionHis )


def test():
	a =(1,2)
	print a[1]
	AllAction =[]
	for x in range(ROW_NUM):
		for y in range(ECO_NUM):
			AllAction += [(x, y)]

	print AllAction

	pass

def ActionSection( Num ):
	Num = 10
	maxNum = Num * Num
	sumVal = 1
	for n in range(maxNum, 0, -2):
		sumVal = sumVal * n
	print    sumVal
	return sumVal

def test():
	sonAction =[(0,1),(1,1),(2,2)]
	avaAction = [(0,1),(1,1),(0,0), (2,3)]

	print listdim(avaAction, sonAction )


	pass

def listdim( list1 , list2 ):  # list1 - list2
	return list(set(list1) - set(list2))

if __name__ == "__main__":
	test()
	#main()

	pass    