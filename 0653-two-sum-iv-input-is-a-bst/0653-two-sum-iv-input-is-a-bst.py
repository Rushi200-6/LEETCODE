class Solution(object):
    def findTarget(self, root, k):     
        class bstiterator:
            def __init__(self,root,reverse):
                self.s=[]
                self.reverse=reverse
                self.pushall(root)
            def pushall(self,node):
                while node:
                    self.s.append(node)
                    if self.reverse:
                        node=node.right
                    else:
                        node=node.left
            def next(self):
                node=self.s.pop()
                val=node.val
                if self.reverse:
                    self.pushall(node.left)
                else:
                    self.pushall(node.right)
                return val
            def hasnext(self):
                return len(self.s)>0
        left=bstiterator(root,False)
        right=bstiterator(root,True)
        i=left.next()
        j=right.next()
        while i<j:
            total=i+j
            if total==k:
                return True
            elif total<k:
                if left.hasnext():
                    i=left.next()
                else:
                    return False
            else:
                if right.hasnext():
                    j=right.next()
                else:
                    return False
        return False
        # arr=[]
        # def ino(node):
        #     if node is None:
        #         return
        #     ino(node.left)
        #     arr.append(node.val)
        #     ino(node.right)
        # ino(root)
        # l,r=0,len(arr)-1
        # while l<r:
        #     t=arr[l]+arr[r]
        #     if t==k:
        #         return True
        #     elif t<k:
        #         l+=1
        #     else:
        #         r-=1
        # return False