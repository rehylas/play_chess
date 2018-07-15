#!/usr/bin/env python
# -*- coding: utf-8 -*-




'''

Node
保存内容： times, wins, values(落子点), UCBVal
点信息： id,  type, leaf no,   level no

输出：
create
setData(Data)
setParent(Node)
addSubNode(Node)
getSubNodeList()

updateTimesWins(isWin)
getUCBVal
setVaule(self, value):

#getSubNodebyVal(  val )
内部


'''

class Node():
    def __init__(self, info=None, data=None ):
        self.data = [ 0,0, () ]   #times, wins, values
        if( data != None ):
            self.data = data
        self.nodeInfo=[  0, 0 ,0, [] ]   #Nodeid,  level ,   parentId, childrenIdList
        if( info != None ):
            self.nodeInfo = info

        self.parent = None
        self.children = []
        pass

    def setData(self,data):
        self.data = data

    def setParent(self, parentNode):
        self.parent = parentNode

    def addChild(self, childNode ):
        self.children += [ childNode ]

    def getSubNodeList(self):
        return self.children


    def setVaule(self, value):
        self.data[2] = value


    def __repr__(self):
        return "nodeInfo: {},  ".format(self.nodeInfo )

    def __eq__(self, other):
        selfVal = "{}".format(self.nodeInfo )
        otherVal = "{}".format(other.nodeInfo)

        if hash(selfVal) == hash(otherVal):
            return True
        return False


'''
Tree
输出：
1.创建
2.获取根节点
3.获取当前节点
4.复位（ 一般 回溯之后 ）
5.loadFile
6.saveFile
7.获取usb最优节点
8.增加新节点
9.移动当前节点

内部：


'''

class Tree():
    ###### 输出
    def __init__(self):
        self.root_Node = Node()
        self.cur_Node = self.root_Node
        self.NodeCount = 1  # 节点+ 叶子数
        pass

    def reset(self):
        self.cur_Node = self.root_Node
        pass

    def load(self, filename ):
        pass

    def save(self, filename):
        pass

    def getRootNode(self):
        return self.root_Node;

    def getCurNode(self):
        return self.cur_Node;

    def getBestUCBNode(self):
        return None

    def addSubNodeToCur_Node(self, subNode):
        pass

    def addBrotherNodeToCur_Node(self, subNode, jump = True):
        pass



    def jump2Level(self,  Level ):
        if( Level == self.cur_Node.nodeInfo[0] ):
            return True
        if( Level < self.cur_Node.nodeInfo[0]  ):
            while( Level < self.cur_Node.nodeInfo[0] ):
                self.jumpup()
            return True

        if (Level > self.cur_Node.nodeInfo[0]):
            while (Level > self.cur_Node.nodeInfo[0]):
                if( self.jumpdown() == None ):
                    return False
        return True

        pass

    #Fail
    def jump2NodeBySite(self, site ):
        pass


###### 内部函数
    def expandNode(self, parentNode, value ):
        childNode = Node()
        childNode.setVaule( value )
        childNode.setParent( parentNode )
        parentNode.addChild( childNode )
        return  childNode

    #ok
    def jumpup(self):
        self.cur_Node = self.cur_Node.parent
        return self.cur_Node
        pass

    #ok
    def jumpdown(self):
        if(  len(     self.cur_Node.children ) ==0  ):
            return None
        self.cur_Node = self.cur_Node.children[0]
        return self.cur_Node


'''
    def jumpbrother(self):
        self.cur_Node = self.cur_Node.parent
        pass
'''

class data():
    ###### 输出
    def __init__(self, val):
        self.info =[1,2,4,val]

        pass

def test():
    d1 = data((1, 0))
    d2 = data((1, 1))
    d3 = data((1, 2))
    d4 = data((1, 3))

    lst = [d1, d2, d3]
    print lst[0].info
    lst[0].info[0] = 100

    print lst[0].info
    print d1.info

    print
    pass

def createTree():
    firstTree = Tree()
    firstTree.getRootNode().nodeInfo = [0,0,0]

    subNode = Node( info=(1,1,1) )
    firstTree.addSubNodeToCur_Node( subNode )

    subNode = Node( info=(2,1,4) )
    firstTree.addSubNodeToCur_Node( subNode )

    subNode = Node( info=(2,2,5) )
    firstTree.addBrotherNodeToCur_Node( subNode )

    subNode = Node( info=(3,1,9) )
    firstTree.addSubNodeToCur_Node( subNode )

    firstTree.jump2Level(1)
    subNode = Node( info=(1,2,2) )
    firstTree.addBrotherNodeToCur_Node( subNode )

    subNode = Node( info=(2,3,6) )
    firstTree.addSubNodeToCur_Node( subNode )

    subNode = Node( info=(3,2,10) )
    firstTree.addSubNodeToCur_Node( subNode )

    subNode = Node( info=(3,2,11) )
    firstTree.addBrotherNodeToCur_Node( subNode )

    firstTree.jumpup()
    subNode = Node( info=(2,4,7) )
    firstTree.addBrotherNodeToCur_Node( subNode )

    subNode = Node( info=(3,4,12) )
    firstTree.addSubNodeToCur_Node( subNode )

    subNode = Node( info=(3,5,13) )
    firstTree.addBrotherNodeToCur_Node( subNode )

    firstTree.jump2Level(1)
    subNode = Node( info=(1,3,3) )
    firstTree.addBrotherNodeToCur_Node( subNode )

    subNode = Node( info=(3,5,8 ) )
    firstTree.addSubNodeToCur_Node( subNode )
    pass

class user(  ):
    def __init__(self,data):
        self.data= data
    def __eq__(self, other):
        if hash(self) == hash(other):
            return True
        return False

    def val(self):
        return hash(self.data)

def test():
    lst = [1,'a', True]
    rec = (1,'a', True)

    print lst
    print rec
    d1 = user('1')
    d2 = user('1')

    print d1.data

    #print (d1 == d2)
    print d1.val()
    print d2.val()

    Node1 = Node(info=(1,1,0,[]))
    Node2 = Node(info=(1, 2, 0, []))
    print Node1
    print (Node1 == Node2 )
    pass




def main():
    pass


if __name__ == "__main__":
	test()
	#main()

	pass