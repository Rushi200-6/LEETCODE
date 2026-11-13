class BSTIterator(object):

    def __init__(self, root):
        self.s=[]
        self.pushALL(root)
    def pushALL(self,node):
        while node:
            self.s.append(node)
            node=node.left
    def next(self):
        node=self.s.pop()
        if node.right:
            self.pushALL(node.right)
        return node.val
    def hasNext(self):
       return len(self.s)>0