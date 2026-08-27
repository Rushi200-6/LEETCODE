from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            n = len(queue)
            level = [0] * n

            for i in range(n):
                node = queue.popleft()

                if left_to_right:
                    level[i] = node.val
                else:
                    level[n - 1 - i] = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)
            left_to_right = not left_to_right

        return result