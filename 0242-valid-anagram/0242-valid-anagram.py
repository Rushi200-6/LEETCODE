class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            if ch not in freq:
                return False
            else:
                if freq[ch]==0:
                    return False
                else:
                    freq[ch]-=1
        return True
        
       

        