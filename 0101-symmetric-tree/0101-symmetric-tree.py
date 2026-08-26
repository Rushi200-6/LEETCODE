class Solution:

    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
       
        if not left and not right:
            
            return True
        if not left or not right:
            return False

        # Values must match, and outer/inner subtrees must mirror each other
        return (
            left.val == right.val
            and self.isMirror(left.left, right.right)
            and self.isMirror(left.right, right.left)
        )
