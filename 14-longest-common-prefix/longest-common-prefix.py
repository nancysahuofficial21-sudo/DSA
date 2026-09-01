class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lens=float('inf')
        for i in range(len(strs)):
            if len(strs[i])<lens:
                lens=len(strs[i])
                prefix=strs[i]
        j=0
        while len(prefix)>0:
            f= True
            for k in strs:
                if not k.startswith(prefix):
                    f=False
                    break
            if f:
                return prefix
            prefix=prefix[:-1]
        return ""
                
        