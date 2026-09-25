class Solution:
    def getRow(self, rowIndex):
        ans = [1]

        for i in range(rowIndex):
            ans.append(ans[-1] * (rowIndex - i) // (i + 1))

        return ans