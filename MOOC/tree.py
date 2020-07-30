from MOOC.TOOLS import Node
from MOOC.TOOLS import Stack
#定义二叉树类
class BinaryTree:
    def __init__(self,rootObj):
        self.key=rootObj
        self.rightChild=None
        self.leftChild=None
    #插入左子树
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    #插入右子树
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key

    #前序遍历
    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    #中序遍历
    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)

#构建二叉堆
class Binheap:
    def __init__(self):
        self.heaplist=[0]
        self.currentsize=0
    #选择根节点中较小的一个
    def minChild(self,i):
        #唯一子节点
        if (i*2)+1>self.currentsize:
            return i*2
        else:
            if self.heaplist[i*2]<self.heaplist[i*2+1]:
                return i*2
            else:
                return i*2+1
    #上浮
    def percup(self,i):
        #判断是否有父节点
        while i//2>0:
            if self.heaplist[i]<self.heaplist[i//2]:
                temp=self.heaplist[i]
                self.heaplist[i]=self.heaplist[i//2]
                self.heaplist[i//2]=temp
            i=i//2
    #下沉
    def percdown(self,i):
        #判断是否与根节点
        while (i*2)<=self.currentsize:
            mc=self.minChild(i)
            if self.heaplist[i]>self.heaplist[mc]:
                temp=self.heaplistp[i]
                self.heaplistp[i]=self.heaplist[mc]
                self.heaplist[mc]=temp
            i=mc

    def insert(self,k):
        self.heaplist.append(k)
        self.currentsize=self.currentsize+1
        self.percup(self.currentsize)


    def delMin(self):
        retval=self.heaplistp[1]
        self.heaplist[1]=self.heaplist[self.currentsize]
        self.currentsize = self.currentsize - 1
        self.heaplist.pop()
        self.percdown(1)
        return retval




#创建表达式解析树
def buildParseTree(fpexp):
    fplist=fpexp.split()
    pStack=Stack()
    eTree=BinaryTree("")
    #入栈下降
    pStack.push(eTree)
    currentTree=eTree
    for i in fplist:
        if i=="(":
            currentTree.insertLeft('')
            #入栈下降
            pStack.push(currentTree)
            currentTree=currentTree.getLeftChild()
        elif i not in ['+',"-","*","/",")"]:
            currentTree.setRootVal(int(i))
            #出栈上升
            parent=pStack.pop()
            currentTree=parent
        elif i in ['+',"-","*","/"]:
            currentTree.setRootVal(i)
            currentTree.insertRight("")
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild()
        elif i==")":
            currentTree=pStack.pop()
        else:
            raise ValueError
    return eTree
#使用递归计算运算树
import operator
def evaluate(parseTree):
    opers={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
    #得到左子树
    leftC=parseTree.getLeftChild()
    #得到右子树
    rightC=parseTree.getRightChild()

    if leftC and rightC:
        fn=opers[parseTree.getRootVal()]
        #计算左子树和右子树的值
        return fn(evaluate(leftC),evaluate(rightC))

    else:
        #没有左右子树，返回值
        return parseTree.getRootVal()

#树的前序遍历递归算法
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

#二叉树的后序遍历
def postorder(tree):
    if tree!=None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

#二叉树的中序遍历
def inorder(tree):
    if tree !=None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


if __name__=="__main__":
    print(" ( 3 + ( 5 * 4 ) )".split())
    r=BinaryTree("a")
    r.insertLeft("b")
    r.insertRight("c")
    r.getLeftChild().setRootVal('d')
    tree=buildParseTree(" ( 3 + ( 5 * 4 ) ) ")
    print(evaluate(tree))
    tree.inorder()
    tree.postorder()