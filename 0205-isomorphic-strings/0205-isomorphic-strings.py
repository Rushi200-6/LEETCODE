class Solution(object):
    def isIsomorphic(self, s, t):
        mapp={}
        mappttos={}
        for i in range(len(s)):
            char_s=s[i]
            char_t=t[i]
            if char_s in mapp:
                if mapp[char_s]!=char_t:
                    return False
            else:
                mapp[char_s]=char_t
            if char_t in mappttos:
                if mappttos[char_t]!=char_s:
                    return False
            else:
                mappttos[char_t]=char_s
        return True

        