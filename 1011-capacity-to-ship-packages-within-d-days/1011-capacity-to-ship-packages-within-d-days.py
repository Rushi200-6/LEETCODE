class Solution(object):
    def shipWithinDays(self, weights, days):
        n=len(weights)
        l=max(weights)
        r=sum(weights)
        while l<=r:
            mid=l+(r-l)//2
            day,load=1,0
            for i in range(0,n):
                if load+weights[i]>mid:
                    day+=1
                    load=weights[i]
                else:
                    load+=weights[i]
            if day<=days:
                r=mid-1
            else:
                l=mid+1
        return l