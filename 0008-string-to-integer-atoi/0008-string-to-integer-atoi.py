class Solution(object):
    def myAtoi(self, s):
        n=len(s)
        # skip the spaces
        i=0
        while i<n and s[i]==" ":
            i=i+1
        # decide the sign
        sign=1
        if i<n:
            if s[i]=="-":
                sign=-1
                i=i+1
            elif s[i]=="+":
                sign=1
                i=i+1
        # conversion
        num=0
        while i<n and s[i].isdigit():
            digit=ord(s[i])-ord("0")
            num=num*10+digit
            
            i=i+1
        num=sign*num
        # rounding
        min=-2**31
        max=2**31-1
        if num>max:
            num=2**31-1
        if num<min:
            num=-2**31
        return num