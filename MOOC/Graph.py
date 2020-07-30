class  Vertex:
    def __int__(self,key):
        self.id=key
        self.connectedTo={}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight

    def __str__(self):
        return str(self.id)+'connectedTo:'+str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


#定义一个图类
class Graph:

    def __init__(self):
        #定义一个字典存储图节点
        self.verList={}
        self.numVertices=0
    #新加顶点
    def addVertex(self,key):
        self.numVertices=self.numVertices+1
        self.newVertex=Vertex(key)
        self.verList[key]=self.newVertex
        return self.newVertex
    #通过key查找顶点
    def getVertex(self,n):
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self,f,t,cost=0):
        if f not in self.verList:
            nv=self.addVertex(f)

        if t not in self.verList:
            nv=self.addVertex(t)

        self.verList[f].addNeighbor(self.verList[t],cost)
    #返回图的所有顶点
    def getVertics(self):
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())

