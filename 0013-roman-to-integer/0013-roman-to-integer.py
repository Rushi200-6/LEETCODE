class Solution(object):
    def romanToInt(self, s):
        r={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res=0
        n=len(s)
        for i in range(0,n):
            if i<n-1 and r[s[i]]<r[s[i+1]]:
                res-=r[s[i]]
            else:
                res+=r[s[i]]
        return res
    # IV=V-I