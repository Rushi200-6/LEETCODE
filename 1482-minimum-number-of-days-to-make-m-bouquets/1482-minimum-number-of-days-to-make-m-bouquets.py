class Solution(object):
    def minDays(self, bloomDay, m, k):
        n=len(bloomDay)
        l=min(bloomDay)
        r=max(bloomDay)
        if n< m*k:
            return -1
        while l<=r:
            mid=l+(r-l)//2
            count=0
            b=0
            for i in range(0,n):
                if bloomDay[i]<=mid:
                    count+=1
                    if k==count:
                        b+=1
                        count=0
                else:
                    count=0
            if b>=m:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
        # nlogn
                
        