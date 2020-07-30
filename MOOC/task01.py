"""
二分查找

"""
def binarySearch(alist,item):
    if len(alist)==0:
        return False
    else:
        midpoint=len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint:],item)

#######################################################################
#冒泡排序
#######################################################################
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp=alist[i+1]
                alist[i+1]=alist[i]
                alist[i]=temp
    return alist

#########################################################################
#选择排序
#########################################################################
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            #记录最大项位置
            if alist[location]>alist[positionOfMax]:
               positionOfMax=location
            temp = alist[fillslot]
            alist[fillslot] = alist[positionOfMax]
            alist[positionOfMax] = temp
    return alist

###########################################################################
#插入排序
###########################################################################
def insertionSort(alist):
    for index in range(1,len(alist)):
        #记录当前值的位置
        curentValue=alist[index]
        position=index
        while position>0 and alist[position-1]>curentValue:
            #将值后移一位
            alist[position]=alist[position-1]
            position=position-1
        alist[position]=curentValue
    return alist

###############################################################################
#希尔排序
##############################################################################
def gapInsertSort(alist,start,gap):
    for index in range(start+gap,len(alist),gap):
        currentvalue=alist[index]
        position=index
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position=position-gap
        alist[position]=currentvalue
    return alist

def shellSort(alist):
    sublistcount=len(alist)//2
    while sublistcount>0:
        for startposition in range(sublistcount):
            gapInsertSort(alist,startposition,sublistcount)
        print("after increments of size {},the list is {}".format(sublistcount,alist))

        sublistcount=sublistcount//2
    return alist


if __name__=="__main__":
    print(binarySearch([1,2,3,4,5,6,7,8,9,10],8))
    print(bubbleSort([23,34,232,344,123,45,65,31,87]))
    print(selectionSort([23,34,232,344,123,45,65,31,87]))
    print(insertionSort([23,34,232,344,123,45,65,31,87]))
    print(shellSort([23,34,232,344,123,45,65,31,87,92,74,96,82]))