class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        l=[]
        dic1={}
        for i in p:
            dic1[i]=dic1.get(i,0)+1
        dic2={}
        m=0
        while m<len(p):
            dic2[s[m]]=dic2.get(s[m],0)+1
            m+=1
        if dic1==dic2:
            l.append(0)
        left=0
        for ri in range(len(p),len(s)):
            dic2[s[left]]-=1
            if dic2[s[left]]==0:
                del dic2[s[left]]
            dic2[s[ri]]=dic2.get(s[ri],0)+1
            if dic2==dic1:
                l.append(left+1)
            left+=1
        return l
            
        