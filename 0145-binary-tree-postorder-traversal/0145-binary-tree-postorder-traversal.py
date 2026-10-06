class Solution(object):
    def postorderTraversal(self, root):
        ans=[]
        curr=root
        st=[]
        while curr or st:
            if curr!=None:
                st.append(curr)
                curr=curr.left
            else:
                temp=st[-1].right
                if temp is None:
                    temp=st.pop()
                    ans.append(temp.val)
                    while st and temp==st[-1].right:
                        temp=st.pop()
                        ans.append(temp.val)

                else:
                    curr=temp
        return ans

        # ans=[]
        # def post(node):
        #     if node is None:
        #         return []
        #     post(node.left)
        #     post(node.right)
        #     ans.append(node.val)
        # post(root)
        # return ans
            