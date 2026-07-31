class Solution(object):
    def rearrangeArray(self, nums):
        n=len(nums)
        ans=[0]*n
        pos=0
        neg=1
        for num in nums:
            if num>0:
                ans[pos]=num
                pos+=2
            if num<0:
                ans[neg]=num
                neg+=2
        return ans

        