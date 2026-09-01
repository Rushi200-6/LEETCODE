class Solution:
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0])
        l,r=0,m-1
        while l<=r:
            mid=l+(r-l)//2
            if target>=matrix[mid][0] and target<=matrix[mid][n-1]:
                low,high=0,n-1
                while low<=high:
                    m=low+(high-low)//2
                    if target==matrix[mid][m]:
                        return True
                    if target<matrix[mid][m]:
                        high=m-1
                    else:
                        low=m+1
                return False
            elif target>matrix[mid][n-1]:
                l=mid+1
            else:
                r=mid-1
        return False
        