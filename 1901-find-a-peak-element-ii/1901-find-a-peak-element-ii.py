class Solution(object):
    def findPeakGrid(self, mat):
        l=0
        r=len(mat)-1
        while l<r:
            mid=l+(r-l)//2

            col=mat[mid].index(max(mat[mid]))
            if mat[mid][col]>mat[mid+1][col]:
                r=mid
            else:
                l=mid+1
        col=mat[l].index(max(mat[l]))
        return [l,col]