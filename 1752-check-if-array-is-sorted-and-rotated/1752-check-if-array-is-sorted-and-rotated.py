class Solution(object):
    def check(self, nums):
        drop=0
        n=len(nums)
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                drop+=1
        return drop<=1
        