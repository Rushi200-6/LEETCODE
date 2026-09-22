class Solution:
    def mySqrt(self, x):
        if x==0:
            return 0
        l=1
        r=x
        res=1
        while l<=r:
            mid=l+(r-l)/2
            m=mid*mid
            if m==x:
                return mid
            elif m<x:
                res=mid
                l=mid+1
            else:
                r=mid-1
        return res