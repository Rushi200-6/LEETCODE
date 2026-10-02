class Solution(object):
    def reverseWords(self, s):
        n=len(s)
        i=0
        ans=""
        s=s[::-1]
        for _ in range(n):
            word=""
            while i<n and s[i]!=" ":
                word+=s[i]
                i+=1
            word=word[::-1]
            if len(word)>0:
                ans+=" "+word
            i+=1
        return ans.strip()