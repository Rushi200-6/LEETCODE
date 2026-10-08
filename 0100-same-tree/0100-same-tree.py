class Solution:
    def isSameTree(self, p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        left=self.isSameTree(p.left,q.left)
        right=self.isSameTree(p.right,q.right)

        return left and right and p.val==q.val
