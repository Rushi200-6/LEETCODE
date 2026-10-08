class Solution:
    def isBalanced(self, root):
        
        def h(node):
            if node is None:
                return True
            left=h(node.left)
            if left==-1:
                return -1
            right=h(node.right)
            if right==-1:
                return -1
            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return h(root)!=-1