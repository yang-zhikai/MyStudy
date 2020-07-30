from MOOC.TOOLS import Stack,Queue,Deque

##################################
'''栈的应用'''
##################################

#括号匹配算法
def parChecker(string):
    s=Stack()
    balanced=True
    index=0
    while index<len(string) and balanced==True:
        symbol=string[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index=index+1

    if balanced==True and s.isEmpty():
        return True
    else:
        return False

#扩展的括号匹配
def parCherk(string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced == True:
        symbol = string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top=s.pop()
                if not match(top,symbol):
                    balanced=False
        index = index + 1

    if balanced == True and s.isEmpty():
        return True
    else:
        return False

def match(open,close):
    opens="([{"
    closes=")]}"
    return opens.index(open)==closes.index(close)


#十进制转二进制
def divideBy2(number):
    remstack=Stack()
    while number>0:
        num=number%2
        remstack.push(num)
        number=number//2
    binString=''
    while not remstack.isEmpty():
        binString=binString+str(remstack.pop())

    return binString

#转换成任意进制
def baseConverter(number,base):
    digits="0123456789ABCDEF"
    remstack=Stack()
    while number>0:
        num=number%base
        remstack.push(num)
        number=number//base
    binString=''
    while not remstack.isEmpty():
        binString=binString+digits[remstack.pop()]

    return binString

#后缀表达式求值
def postfixEval(postfixeval):
    s=Stack()
    tokenlist=postfixeval.split()

    for token in tokenlist:
        if token in "012346789":
            s.push(token)
        else:
            operand2=s.pop()
            operand1=s.pop()
            result=domath(token,operand1,operand2)
            s.push(result)
    return s.pop()

def domath(op,op1,op2):
    if op=="+":
        return op1+op2
    elif op=="-":
        return op1-op2
    elif op=="*":
        return op1*op2
    else:
        return op1/op2


#####################################
'''队列的应用'''

#####################################

#热土豆问题
def hotPhoto(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


from MOOC.TOOLS import Printer,Task,newPrintTask

def simulation(numSecons,pagePerMinute):
    labprinter=Printer(pagePerMinute)
    printQueue=Queue()
    waitingtimes=[]

    for currentSecond in range(numSecons):
        if newPrintTask():
            task=Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask=printQueue.dequeue()
            waitingtimes.append()



#######################################
#判断回文词
#######################################

def check(String):
    tokens=String.split()
    deque=Deque()
    tokens_front=[]
    tokens_rear=[]
    for i in tokens:
        deque.addRear(i)
    while deque.size()!=1 or deque.size()!=0:
        token_front=deque.removeFront()
        token_rear=deque.removeRear()
        tokens_front.append(token_front)
        tokens_rear.append(token_rear)
    if tokens_rear==tokens_front:
        return True
    else:
        return False



if __name__=="__main__":

    print(parChecker("(((())))"))
    print(parChecker("((()))))"))
    print(parCherk("{{[[(())]]}}"))
    print(divideBy2(120))
    print(baseConverter(255,16))
    print(hotPhoto(namelist=["Bob","Tom","Smart","Sam","Tim","Jordan","Ball","Loken"],num=7))
