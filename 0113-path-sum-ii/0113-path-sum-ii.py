class Solution:
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if node is None:
                return

            path.append(node.val)
            remaining -= node.val

            # Check if node is a leaf
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path[:])

            else:
                dfs(node.left, remaining, path)
                dfs(node.right, remaining, path)

            # Backtracking
            path.pop()

        dfs(root, targetSum, [])

        return result