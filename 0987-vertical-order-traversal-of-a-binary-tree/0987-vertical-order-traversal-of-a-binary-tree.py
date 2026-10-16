class Solution(object):
    def verticalTraversal(self, root):
        nodes=defaultdict(list)
        q=deque([(root,0,0)])
        while q:
            node,row,col=q.popleft()
            nodes[col].append((row,node.val))
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
        ans=[]
        for col in sorted(nodes):
            values=sorted(nodes[col])
            ans.append([val for row,val in values])
        return ans