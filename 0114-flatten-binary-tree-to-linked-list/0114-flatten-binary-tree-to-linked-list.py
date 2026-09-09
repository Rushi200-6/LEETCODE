class Solution:
    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        right = root.right

        root.right = root.left
        root.left = None

        curr = root
        while curr.right:
            curr = curr.right

        curr.right = right
    # tree