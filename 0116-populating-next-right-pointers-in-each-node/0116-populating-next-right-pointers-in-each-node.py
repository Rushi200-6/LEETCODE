class Solution:
    def connect(self, root):
        if root is None:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost

            while head:
                
                head.left.next = head.right

               
                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root