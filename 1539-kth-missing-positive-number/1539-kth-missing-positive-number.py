class Solution(object):
    def findKthPositive(self, arr, k):
        n=len(arr)
        l=0
        r=n-1
        while l<=r:
            mid=l+(r-l)//2
            missing=arr[mid]-(mid+1)
            if missing<k:
                l=mid+1
            else:
                r=mid-1
        ans=l+k
        return ans
        