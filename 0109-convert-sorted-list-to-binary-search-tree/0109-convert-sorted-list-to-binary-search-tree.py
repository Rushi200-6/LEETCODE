class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        prev = None
        slow = head
        fast = head

        # Find middle node
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Disconnect left half
        prev.next = None

        # Middle becomes root
        root = TreeNode(slow.val)

        # Build left and right subtrees
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root