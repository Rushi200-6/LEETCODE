class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        a=len(nums1)
        if a%2==0:
            i=a // 2
            j=(a//2)-1
            median=(nums1[i]+nums1[j])/2.0
        else:
            i=a//2
            median=nums1[i]
        return median