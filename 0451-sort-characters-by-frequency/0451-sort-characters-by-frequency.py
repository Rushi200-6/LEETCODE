class Solution(object):
    def frequencySort(self, s):
        res=""
        hash_map={}
        for ch in s:
            hash_map[ch]=hash_map.get(ch,0)+1
        sorted_ch=sorted(hash_map.items(),key=lambda x:x[1],reverse=True)
        for ch,freq in sorted_ch:
            res+=(ch*freq)
        return res

        