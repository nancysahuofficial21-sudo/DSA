class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        freq={}
        res=0
        maxfreq=0
        for ri in range(len(s)):
            freq[s[ri]]=freq.get(s[ri],0)+1
            maxfreq=max(maxfreq,freq[s[ri]])
            while (ri-left+1) - maxfreq>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            res=max(res,ri-left+1)
        return res


        

        