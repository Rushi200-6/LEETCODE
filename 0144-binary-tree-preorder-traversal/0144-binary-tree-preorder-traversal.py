class Solution(object):
    def preorderTraversal(self, root):
        ans=[]
        curr=root
        st=[]
        if root is None:
            return []
        while curr or st:
            if curr:
                ans.append(curr.val)
                st.append(curr.right)
                curr=curr.left
            else:
                curr=st.pop()
        return ans

        # ans=[]
        # def pre(node):
        #     if node is None:
        #         return []
        #     ans.append(node.val)
        #     pre(node.left)
        #     pre(node.right)
        # pre(root)
        # return ans