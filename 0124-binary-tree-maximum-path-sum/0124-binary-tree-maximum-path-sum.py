class Solution(object):
    def maxPathSum(self, root):
        m=[float("-inf")]
        def sum(node):
            
            if node is None:
                return 0
            left=sum(node.left)
            if left<0:
                left=0
            right=sum(node.right)
            if right<0:
                right=0 
            m[0]=max(m[0],left+right+node.val)
            return node.val+max(left,right)
        sum(root)
        return m[0]
        