class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        def left(node):
            h=0
            while node:
                h+=1
                node=node.left
            return h
        def right(node):
            h=0
            while node:
                h+=1
                node=node.right
            return h
        lh=left(root)
        rh=right(root)
        if lh==rh:
            return (1<<lh)-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        # if  root is None:
        #     return 0
        # left=self.countNodes(root.left)
        # right=self.countNodes(root.right)
        # return left+right+1
        
             
        # if root is None:
        #     return 0
        # q=deque([root])
        # ans=0
        # while q:
        #     for _ in range(len(q)):
        #         node=q.popleft()
        #         ans+=1
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return ans  


        