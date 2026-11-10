class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        # if (p.val>root.val and q.val<root.val) and (p.val<root.val and q.val>root.val):
        #      return root
        if p.val<root.val and q.val<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p.val>root.val and q.val>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
    # to avoid or eliminate  the recursive stack space
    # while root:
    #     if p.val<root.val and q.val<root.val:
    #         root=root.left
    #     elif p.val>root.val and q.val>root.val:
    #         root=root.right
    #     else:
    #         return root
    # return None