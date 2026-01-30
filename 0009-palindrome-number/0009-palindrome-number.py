class Solution(object):
    def isPalindrome(self, x):
        a=abs(x)
        s=0
        while(a!=0):
            d=a%10
            s=s*10+d
            a=a//10
        if(s==x):
            return True
        else:
            return False
        