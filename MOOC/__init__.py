#递归
def listSum(numlist):
    theSum=0
    for i in numlist:
        theSum=i+theSum
    return theSum
#用递归的方法求和
def Listsum(numlist):
    if len(numlist)==1:
        return numlist[0]
    else:
        return numlist[0]+Listsum(numlist[1:])

#任意进制的转换
def toStr(n,base):
    convertString="0123456789ABCDEF"
    if n<base:
        return convertString[n]
    else:
        return toStr(n//base,base)+convertString[n%base]

import turtle
t=turtle.Turtle()
def drawSpiral(t,linelen):
    if linelen>0:
        t.forward(linelen)
        t.right(90)
        t.speed(1)
        drawSpiral(t,linelen-5)


def getMid(p1,p2):
    return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)

def drawTriangle(points,color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

#画谢尔宾斯基三角形
def sierpinski(degree,points):
    colormap=['blue','red','green','white','yellow','orange']
    drawTriangle(points,colormap[degree])
    if degree>0:
        sierpinski(degree-1,
                   {
                    'left':points['left'],
                    'top':getMid(points['left'],points['top']),
                    'right':getMid(points['left'],points['right'])
                   }
                   )
        sierpinski(degree-1,
                   {
                    'left':getMid(points['left'],points['top']),
                    'top':points['top'],
                    'right':getMid(points["right"],points['top'])
                    }
                   )

        sierpinski(degree-1,
                   {
                       'left':getMid(points["left"],points["right"]),
                       'top':getMid(points['top'],points['right']),
                       'right':points['right']
                   }
                   )

def moveDisk(disk,fromtower,totower):
    print('Moving disk[{disk}] from {fromtower} to {totower}')

#汉诺塔问题
def moveTower(height,fromtower,withtower,totower):
    if height>=1:
        moveTower(height-1,fromtower,totower,withtower)
        moveDisk(height,fromtower,totower)
        moveTower(height,withtower,fromtower,totower)


if __name__ == "__main__":
    print(listSum([1,3,5,7,9]))
    print(Listsum([1,3,5,7,9]))
    print(toStr(255,2))

    #
    # points={"left":(-200,-100),
    #         'top':(0,200),
    #         'right':(200,-100)}
    #
    # sierpinski(5,points)
    #
    # turtle.done()

    moveTower(5,"#1","#2","#3")