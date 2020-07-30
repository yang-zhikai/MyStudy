class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key,value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False
    def __delitem__(self, key):
        self.delete(key)
    #删除节点
    def delete(self,key):
        if self.size>1:
            #从根节点开始找
            node2Move=self._get(key,self.root)
        #如果找到，则删除
            if node2Move:
                self.remove(node2Move)
                self.size=self.size-1
        #如果找不到，则报错
            else:
                raise KeyError("Error,key not in tree")
        #如果只有一个根节点
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size=self.size-1

        else:
            raise KeyError("Error,key not in tree")

    def remove(self,currentNode):
        #第一种情况，删除的节点是叶节点
        if currentNode.isleaf():
            if currentNode==currentNode.parent.leftChild:
                currentNode.parent.leftChild=None

            else:
                currentNode.parent.rightChild=None

    #寻找节点
    def get(self,key):
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None

        if currentNode.key==key:
            return currentNode

        elif key<self.currentNode.key:
            return self._get(key,currentNode.leftChild)

        elif key>self.currentNode.key:
            return self._get(key,currentNode.rightChild)

    #插入节点
    def put(self,key,val):
        #若排序树不为空，则插入
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root=TreeNode(key,val)
        self.size=self.size+1

    # 递归插入
    def _put(self,key,val,currentNode):
        #如果值小于当前解点的值
        if key < currentNode.key:
            #如果当前节点有左子树，则进行递归插入
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
        #如果key大于当前节点的值
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)




class TreeNode:
    def __init__(self,key,val,parent=None,
                 left=None,right=None):
        self.key=key
        self.payload=val
        self.leftChild=left
        self.rightChild=right
        self.parent=parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild==self

    def isRightChild(self):
        return self.parent and self.parent.rightChild==self

    def isRoot(self):
        return self.parent

    def isleaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChild(self):
        return self.rightChild or self.leftChild

    def hasBothChild(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key=key
        self.payload=value
        self.leftChild=lc
        self.rightChild=rc
        if self.hasRightChild():
            self.rightChild.parent=self
        if self.hasLeftChild():
            self.leftChild.parent=self


