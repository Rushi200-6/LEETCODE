class Solution:
    def isSameTree(self, p,q):

        if not p and not q:
            return True
        
        
        if not p or not q:
            return False
        
       
        if p.val != q.val:
            return False
        
        # Recursive Step: Check if both left subtrees and right subtrees match
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
