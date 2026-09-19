class Solution(object):
    def majorityElement(self, nums):
        cd1=None
        cd2=None
        n=len(nums)
        c1=0
        c2=0
        res=[]
        for num in nums:
            if c1==0 and num!=cd2:
                cd1=num
                c1=1
            elif c2==0 and num!=cd1:
                cd2=num
                c2=1
            elif num==cd1:
                c1+=1
            elif num==cd2:
                c2+=1
            else:
                c1-=1
                c2-=1
        c1=0
        c2=0
        for num in nums:
            if cd1==num:
                c1+=1
            if cd2==num:
                c2+=1
        mm=n//3
        if c1>mm:
            res.append(cd1)
        if c2>mm:
            res.append(cd2)
        
        return res


        # nums.sort()
        # n=len(nums)
        # count=0
        # candidate=None
        # res=[]
        # for num in nums:
        #     if count==0:
        #         candidate=num
        #     if candidate==num:
        #         count+=1
        #         if count>n//3 and num not in res:
        #             res.append(num)
        #     else:
        #         candidate=num
        #         count=1
        #         if count>n//3:
        #             res.append(num)
        # return res
