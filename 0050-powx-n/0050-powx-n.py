class Solution(object):
    def myPow(self, x, n):
        # if n==0:
        #     return 1
        # if n<0:
        #     x=1/x
        #     n=-n
        # result=1
        # while n>0:
        #     if n%2==1:
        #         result*=x
        #     x*=x
        #     n=n//2
        # return result
        
        # by recursive method
        def help(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            res=help(x,n//2)
            if n%2==0:
                return res*res
            else:
                return res*res*x
        if n<0:
            return 1/help(x,-n)
        return help(x,n)