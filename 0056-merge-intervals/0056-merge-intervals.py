class Solution:
    def merge(self, intervals):
        n=len(intervals)
        intervals.sort()
        res=[]
        for i in range(0,n): 
            if len(res)==0 or intervals[i][0]>res[-1][1]:
                res.append(intervals[i])
            else:
                res[-1][1]=max(res[-1][1],intervals[i][1])
        return res
