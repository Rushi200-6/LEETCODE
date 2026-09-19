class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        n=len(nums)
        count=0
        candidate=None
        res=[]
        for num in nums:
            if count==0:
                candidate=num
            if candidate==num:
                count+=1
                if count>n//3 and num not in res:
                    res.append(num)
            else:
                candidate=num
                count=1
                if count>n//3:
                    res.append(num)
        return res
