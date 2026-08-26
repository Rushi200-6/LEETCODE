



class Solution:

    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])  # Initialize queue with root

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Queue the children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)  # Add level snapshot to result

        return result
