class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n=len(nums)
        closest=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            l,r=i+1,n-1
            while l<r:
                curr_sum=nums[i]+nums[l]+nums[r]
                if abs(curr_sum-target)<abs(closest-target):
                    closest=curr_sum
                if curr_sum<target:
                    l+=1
                elif curr_sum>target:
                    r-=1
                else:
                    return target
        return closest
                
        