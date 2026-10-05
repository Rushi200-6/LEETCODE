class Solution:
    def inorderTraversal(self, root):
        res=[]
        curr=root
        while curr!=None:
            if curr.left==None:
                res.append(curr.val)
                curr=curr.right
            else:
                lc=curr.left
                while lc.right and lc.right!=curr:
                    lc=lc.right
                if lc.right ==None:
                    lc.right=curr
                    curr=curr.left
                else:
                    lc.right=None
                    res.append(curr.val)
                    curr=curr.right
        return res



        # res=[]
        # def inorder(node):
            
        #     if node is None:
        #         return []
        #     inorder(node.left)
        #     res.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # return res