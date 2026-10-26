class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if root==p or root==q:
            return root
        leftlca=self.lowestCommonAncestor(root.left,p,q)
        rightlca=self.lowestCommonAncestor(root.right,p,q)

        if leftlca and rightlca:
            return root
        elif leftlca!=None:
            return leftlca
        else:
            return rightlca

        