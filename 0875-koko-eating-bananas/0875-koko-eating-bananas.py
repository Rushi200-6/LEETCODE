class Solution(object):
    def minEatingSpeed(self, piles, h):
        l,r=1,max(piles)
        while l<=r:
            mid=l+(r-l)//2
            hours=0
            for pile in piles:
                hours+=(pile+mid-1)//mid
            if hours<=h:
                r=mid-1
            else:
                l=mid+1
        return l


