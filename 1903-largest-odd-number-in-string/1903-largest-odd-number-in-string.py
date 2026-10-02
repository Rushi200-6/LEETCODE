class Solution(object):
    def largestOddNumber(self, num):
        res=""
        i=len(num)-1
        while i>=0:
            if int(num[i])%2==1:
                # if(ord(num[i])-ord("0"))%2==1:
                res=num[:i+1]
                break
            i-=1
        return res