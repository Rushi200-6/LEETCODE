class Solution(object):
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0
        q=deque([(root,0)])
        maxwidth=0
        while q:
            level_size=len(q)
            first=q[0][1]
            last=q[-1][1]
            maxwidth=max(maxwidth,last-first+1)
            for _ in range(level_size):
                node,idx=q.popleft()
                if node.left:
                    q.append((node.left,2*idx+1))
                if node.right:
                    q.append((node.right,2*idx+2))
        return maxwidth