class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        # left subtree
        root.left=self.buildTree(preorder[1:index+1],
        inorder[:index])

        # right subtree

        root.right=self.buildTree(
            preorder[index+1:],
            inorder[index+1:]
        )

        return root

