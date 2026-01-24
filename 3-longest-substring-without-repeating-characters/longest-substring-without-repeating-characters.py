class Solution:
    def lengthOfLongestSubstring(self, s):
        m=0
        n=len(s)
        for i in range(0,n):
            c=set()
            for j  in range(i,n):
                if s[j] in c:
                    break
                m=max(m,j-i+1)
                c.add(s[j])
        return m
        