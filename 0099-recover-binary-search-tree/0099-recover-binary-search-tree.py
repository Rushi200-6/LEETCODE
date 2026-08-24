class Solution:
    def recoverTree(self, root):
        # Pointers to track the two swapped nodes and the preceding node
        first = second = prev = None
        curr = root
        
        while curr:
            if curr.left is None:
                # Process the current node
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                # Move to the right child
                curr = curr.right
            else:
                # Find the inorder predecessor of curr
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    # Create a temporary link to the parent
                    predecessor.right = curr
                    curr = curr.left
                else:
                    # Break the temporary link to restore original structure
                    predecessor.right = None
                    
                    # Process the current node
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    
                    # Move to the right child
                    curr = curr.right
                    
        # Swap the values of the two mismatched nodes back to their correct positions
        if first and second:
            first.val, second.val = second.val, first.val
