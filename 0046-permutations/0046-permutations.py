class Solution(object):
    def permute(self, nums):
        result=[]
        def backtrack(path):
            if path==len(nums):
                result.append(nums[:])
                return
            for i in range(path,len(nums)):
                nums[path],nums[i]=nums[i],nums[path]
                backtrack(path+1)
                nums[path],nums[i]=nums[i],nums[path]
        backtrack(0)
        return result