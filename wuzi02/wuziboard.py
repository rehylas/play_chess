#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: hylas zhang

import turtle
from enum import Enum



class PotColor(Enum):
    Black = 1
    White = 2

import time
class WuziBoard(object):
    def __init__(self, RowNum):
        turtle.speed(9)
        turtle.hideturtle()
        self.RowNum = RowNum
        self.halfDim = 500 /(RowNum-1)/2.0
        pass

    def drawBoard(self, ActionHis =None):
        turtle.screensize(400, 400, "white")
        turtle.title('五子棋')
        turtle.home()
        turtle.speed(0)


        for i in range( self.RowNum ):

            x = 0 - 250 + i * ( self.halfDim ) *2
            y = 0 -250
            turtle.penup()
            turtle.setpos(x, y)
            turtle.pendown()
            turtle.goto(x, y + 500)



        for i in range( self.RowNum ):
            x = 0 - 250
            y = 0 -250 + i * ( self.halfDim ) *2
            turtle.penup()
            turtle.setpos(x, y)
            turtle.pendown()
            turtle.setpos(x+500, y)

        turtle.speed(5)
        if( ActionHis != None):
            self.drawNow( ActionHis )

        turtle.done()

        pass

    def action2potxy(self, action):
        x = 0 - 250 + action[0]*self.halfDim*2
        y = 0 - 250 + action[1]*self.halfDim*2
        return x,y

    def drawNow(self, RunAction ):

        for potsite in RunAction:

            x,y = self.action2potxy( ( potsite[0], potsite[1] ) )
            turtle.penup()
            turtle.setpos(x, y)
            turtle.pendown()
            if( potsite[2] != PotColor.Black ) :
                turtle.dot(15,"Red")
            else:
                turtle.dot(15, "Black")

            if( potsite ==  RunAction[len(RunAction) - 1 ] ):
                if (potsite[2] != PotColor.Black):
                    turtle.dot(25, "Red")
                else:
                    turtle.dot(25, "Black")

        pass

    def drawAction(self):
        pass

    pass

def main():
    ActionHis =[ (0,1,1), (1,1,2), (5,1,1),  ]
    wuziBoard = WuziBoard( 6 )
    wuziBoard.drawBoard( ActionHis )

    pass


if __name__ == "__main__":
	#test()
	main()




