#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: hylas zhang

import numpy as np;
import random

'''

Node  class

data
data： []
nodeinfo： id,   level, parentId, childrenIdList    [  0, 0, 0, []  ]
childrenIdList  save to file  : [1,2,3,4]  ==>  1,2,3,4

export function：
create
setData(Data)
setParent(Node)
addSubNode(Node)
getSubNodeList()

in function:

'''

class Node():
    def __init__(self, info=None, data=None, infodata = None ):
        if( infodata != None ):
            info = infodata[0:3] +[[]]
            data = infodata[3:]
            self.info = info
            self.data = data
            pass

        self.data = ['']       #[ 0,0, '' ]   #times, wins, values
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

    def getDataInfo(self):
        dataList = [self.nodeInfo[0],self.nodeInfo[1],self.nodeInfo[2]]  +self.data
        return dataList

    def getData(self):
        return self.data

    def getInfo(self):
        return self.nodeInfo

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
export function：
1.create
2.getRootNode
3.getCurNode
4.reset（ 一般 回溯之后 ）
5.loadFile
6.saveFile
7.addNewNodeInCurNode


7.获取usb最优节点
8.增加新节点
9.移动当前节点

内部：


'''

class Tree( object ):
    ###### 输出
    def __init__(self):
        self.root_Node = Node()
        self.cur_Node = self.root_Node
        self.NodeCount = 1  # 节点+ 叶子数 + 1
        pass

    def reset(self):
        self.cur_Node = self.root_Node
        pass

    def load(self, filename = None ):
        if(  filename == None ):
            filename = './data.npy'
        npData2 = np.load( filename )
        lst2 = npData2.tolist()
        for node in lst2:
            info = node[0:3]
            data = node[3:]
            if( info[0] == 0  ):
                continue
            print 'want to add:'
            print node


            if( info[2] == self.cur_Node.nodeInfo[0] ):
                self.addSubNodeToCur_Data(data, NodeId = info[0] )
                continue

            #self.cur_Node
            count = 10
            while( info[2] != self.cur_Node.nodeInfo[0] ) :

                ret = self.moveUp()

                if( ret == False ):
                    print 'error ......'
                    return

                continue

            self.addSubNodeToCur_Data(data, NodeId = info[0])

        self.printTree()
        pass

    def save(self, filename = None ):
        if (filename == None):
            filename = './data.npy'

        nodeLst = self.fetchAllNode()
        dataList =[]
        for node in nodeLst :
            print node
            dataList += [ node.getDataInfo() ]
    #        Node.
        pass

        npData = np.array( dataList )
        np.save(filename, npData )

        '''
        npData2 = np.load( './data.npy' )
        lst2 = npData2.tolist()
        print 'lst2:', lst2
      '''

    def printTree(self):
        nodeLst = self.fetchAllNode()
        for node in nodeLst :
            print node.getDataInfo()
        pass

    def getRootNode(self):
        return self.root_Node;

    def getCurNode(self):
        return self.cur_Node;

    # nodeinfo： id, level, parentId, childrenIdList[0, 0, 0, []]
    def addSubNodeToCur_Node(self, subNode, isMoveToSub = True ):
        newNodeId = self.NodeCount
        self.NodeCount += 1
        self.cur_Node.children += [subNode]
        self.cur_Node.nodeInfo[3] += [ newNodeId ]

        subNode.parent = self.cur_Node
        subNode.nodeinfo[0] = newNodeId
        subNode.nodeinfo[1] = self.cur_Node.nodeInfo[1] +1
        subNode.nodeinfo[2] = self.cur_Node.nodeInfo[0]
        subNode.nodeinfo[3] = []
        if( isMoveToSub ):
            self.cur_Node = subNode

        pass

    def addSubNodeToCur_Data(self,  data, NodeId = 0, isMoveToSub = True ):
        subNode = Node(data=data)

        if(NodeId == 0 ):
            newNodeId = self.NodeCount
        else:
            newNodeId = NodeId
        self.NodeCount += 1
        self.cur_Node.children += [subNode]
        self.cur_Node.nodeInfo[3] += [ newNodeId ]

        subNode.parent = self.cur_Node

        subNode.nodeInfo[0] = newNodeId
        subNode.nodeInfo[1] = self.cur_Node.nodeInfo[1] +1
        subNode.nodeInfo[2] = self.cur_Node.nodeInfo[0]
        subNode.nodeInfo[3] = []
        #print 'addSubNodeToCur_Data, now in :', self.cur_Node.nodeInfo[0]
        if( isMoveToSub ):
            self.cur_Node = subNode

        #print 'addSubNodeToCur_Data, now in :', self.cur_Node.nodeInfo[0]

    def moveToNode(self,nodeId ):
        node = self.serachNodeId( self.root_Node, nodeId)
        if (node!= None):
            self.cur_Node = node
            return node
        else:
            return None
        pass

    def moveToNode_byNode(self, node ):
        self.cur_Node = node
        pass

    def fetchAllNode(self):
        return self.touchAllNode( self.getRootNode() )
        pass

    #  in function
    def touchAllNode(self, thisNode):
        allNode = [ thisNode ]
        for node in thisNode.children :
            allNode += self.touchAllNode( node )

        return  allNode

    def serachNodeId(self, thisNode, nodeId):
        if( thisNode.nodeInfo[0] == nodeId ):
            return thisNode
        else:
            for node in thisNode.children :
                ret = self.serachNodeId(node , nodeId )
                if( ret != None ):
                    return ret

        return None

    ###### 内部函数
    def moveUp(self):
        if(  self.cur_Node.nodeInfo[0] == 0 ):
            print 'moveUp error'
            return False

        self.cur_Node = self.cur_Node.parent;
        return True

    ######## test
    def demo1(self):
        data = ['{}'.format(  random.random() * 10000 )]
        self.addSubNodeToCur_Data( data )

        self.moveUp();
        data = ['{}'.format(  random.random() * 10000 )]
        self.addSubNodeToCur_Data( data )

        self.save()
        pass

    def deom2(self):
        self.load()


#  下100局， 拓展棋谱
def testWzTree():
    '''
    生成 落子树
    '''
    tree = Tree()
    for i in range(100):
        WzOne( tree )

    tree.printTree()
    tree.save()

    #读取树
    print '------------------------------------------------'
    tree2 = Tree()
    tree2.load()
    tree2.printTree()
    pass


#  下一局，   随机选一个点，  下满棋盘
def WzOne( tree ):
    tree.reset()    #让树当前节点回到根节点
    avilAction = [(0, 0), (0, 1), (1, 0), (1, 1)]    # 4个落子点
    while( len(avilAction) >0 ):  #无落子点
        action = random.choice(avilAction)   #随机一个落子点
        avilAction.remove(action)

        data = list( action )
        # 遍历当前前节点的子节点， 如果已经存在该落子点， 则跳到子节点
        # 如果当前节点的子节点， 无该落子点， 则增加一个子节点
        isExist = False
        for node in tree.cur_Node.children :
            if( node.getData() == data ):
                isExist = True
                tree.moveToNode_byNode( node )
                break
        if( isExist == False ):
            tree.addSubNodeToCur_Data(data)

    pass





def test():
    testWzTree()
    return

    tree = Tree()
    tree.test()
    return


if __name__ == "__main__":
    test()