class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left=0
        dic1={}
        dic2={}
        minlen=float('inf')
        start=0
        for i in t:
            dic1[i]=dic1.get(i,0)+1
        r=len(dic1)
        have=0
        for ri in range(len(s)):
            if s[ri] in dic1:
                dic2[s[ri]]=dic2.get(s[ri],0)+1
            
                if dic2[s[ri]]==dic1[s[ri]]:
                    have+=1
            
            while have==r:
                if minlen>ri-left+1:
                    minlen=ri-left+1
                    start=left
                
                if s[left] in dic1:
                    dic2[s[left]]-=1
                    if dic2[s[left]]<dic1[s[left]]:
                        have-=1
                left+=1
        return s[start:start+minlen] if minlen!=float('inf') else ""

        