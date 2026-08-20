# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n) :
        if n == 0:
            return []
        
        memo = {}
        
        def helper(start, end):
            # Base case: if start exceeds end, return a list containing None
            if start > end:
                return [None]
            
            # Return cached result if already calculated
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            
            # Pick each number as a root
            for i in range(start, end + 1):
                # Generate all valid left and right subtrees recursively
                left_trees = helper(start, i - 1)
                right_trees = helper(i + 1, end)
                
                # Combine every left subtree with every right subtree for root 'i'
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
            
            # Store result in memo dictionary
            memo[(start, end)] = all_trees
            return all_trees
        
        return helper(1, n)
