class Solution(object):
    def diameterOfBinaryTree(self, root):
        ans=[0]
        def D(node):
            # nonlocal ans
            if node is None:
                return 0
            left=D(node.left)
            right=D(node.right)
            
            ans[0]=max(ans[0],left+right)
            return 1+max(left,right)
            
        D(root)
        return ans[0]
        