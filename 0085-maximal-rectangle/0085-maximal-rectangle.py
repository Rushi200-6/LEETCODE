class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        n = len(matrix[0])
        heights = [0] * n
        max_area = 0
        
        for row in matrix:
            
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            
            
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        heights.pop()  
        return max_area