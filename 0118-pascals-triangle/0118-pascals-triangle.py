class Solution(object):
    def generate(self, numRows):
        res=[[1]]
        n=numRows
        for i in range(n-1):
            temp=[0]+res[-1]+[0]
            curr=[]
            for j in range(len(res[-1])+1):
                curr.append(temp[j]+temp[j+1])
            res.append(curr)
        return res

        #two pointers from starting