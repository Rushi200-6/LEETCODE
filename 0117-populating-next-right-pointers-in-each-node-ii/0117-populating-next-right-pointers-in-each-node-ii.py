
class Solution:
    def connect(self, root):
        if not root:
            return None

        q = deque([root])

        while q:
            n = len(q)
            prev = None

            for i in range(n):
                node = q.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            prev.next = None

        return root