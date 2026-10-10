class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q=deque([root])
        ans=[]
        lr=True
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not lr:
                level.reverse()
            ans.append(level)
            lr=not lr
        return ans