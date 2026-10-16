class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        def v(node,level,ans):
            if len(ans)==level:
                ans.append(node.val)
            if node.right:
                v(node.right,level+1,ans)
            if node.left:
                v(node.left,level+1,ans)
        ans=[]
        v(root,0,ans)
        return ans