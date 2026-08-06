class Solution:
    def inorderTraversal(self, root):
        ans = []
        curr = root

        while curr:
            if curr.left is None:
                ans.append(curr.val)
                curr = curr.right
            else:
                # Find inorder predecessor
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right

                if pred.right is None:
                    # Create a temporary thread
                    pred.right = curr
                    curr = curr.left
                else:
                    # Remove the thread
                    pred.right = None
                    ans.append(curr.val)
                    curr = curr.right

        return ans