class Solution:
    def isInterleave(self, s1, s2, s3):
        
        if len(s1) + len(s2) != len(s3):
            return False
            
        
        if len(s1) < len(s2):
            s1, s2 = s2, s1
            
        len1, len2 = len(s1), len(s2)
        
        
        dp = [False] * (len2 + 1)
        dp[0] = True
        
        
        for j in range(1, len2 + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        
        for i in range(1, len1 + 1):
            
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            
            for j in range(1, len2 + 1):
                
                s3_idx = i + j - 1
                

                take_s1 = dp[j] and s1[i - 1] == s3[s3_idx]
                take_s2 = dp[j - 1] and s2[j - 1] == s3[s3_idx]
                
                dp[j] = take_s1 or take_s2
                
        return dp[len2]
