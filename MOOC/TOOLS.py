import random
#定义一个栈类
class Stack:
    def __init__(self):
        self.item=[]

    def isEmpty(self):
        return self.item==[]

    def push(self,item):
        self.item.append(item)

    def pop(self):
        return  self.item.pop()

    def peek(self):
        return self.item[-1]

    def size(self):
        return len(self.item)


#定义一个队列类
class Queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#定义一个双端队列
class Deque:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

#定义一个节点
class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data=newdata

    def setNext(self,newnext):
        self.next=newnext

#定义一个链表
class UnorderList:
    def __init__(self):
        self.head=None

    def isEmpty(self):
        return self.head==None

    def add(self,item):
        current=self.head
        previous=None
        stop=False
        while current!=None and not stop:
            if current.getData()>item:
                stop=True
            else:
                previous=current
                current=current.getNext()

        temp=Node(item)
        if previous==None:
            temp.setNext(self.head)
            self.head=temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    #链表长度
    def size(self):
        count=0
        current=self.head
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    #寻找节点
    def search(self,item):
        current=self.head
        found=False
        while current!=None and not found:
            if current.getData==item:
                found=True
            else:
                current=current.getNext()
        return found
    #删除节点
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current.setNext(current.getNext())
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
#定义一个有序链表
class OrderList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        # 链表长度

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count
        # 寻找节点

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData == item:
                found = True
            else:
                current = current.getNext()
        return found
        # 删除节点

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current.setNext(current.getNext())
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


#定义一个打印机类
class Printer:
    def __init__(self,ppm):
        #打印速率/分钟
        self.pagerate=ppm
        self.currentTask=None
        self.timeRemaining=0
    #打印一秒
    def tick(self):
        if self.currentTask!=None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask=None

    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False

    def startnext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining=newtask.getPages()*60/self.pagerate
#定义打印任务
class Task:
    def __init__(self,time):
        #生成时间
        self.timestamp=time
        #打印页数
        self.pages=random.randint(1,21)

    def getstamp(self):
        return self.timestamp

    def getpages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime-self.timestamp
#定义是否生成打印任务
def newPrintTask():
    num=random.randint(1,181)
    if num==180:
        return True
    else:
        return False


