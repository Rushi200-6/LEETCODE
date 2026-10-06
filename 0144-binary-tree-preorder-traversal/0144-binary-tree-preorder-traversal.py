class Solution(object):
    def preorderTraversal(self, root):
        ans=[]
        def pre(node):
            if node is None:
                return []
            ans.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(root)
        return ans