class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root