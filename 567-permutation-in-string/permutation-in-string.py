class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        dic1={}
        for i in s1:
            dic1[i]=dic1.get(i,0)+1
        dic2={}
        m=0
        while m<len(s1):
            dic2[s2[m]]=dic2.get(s2[m],0)+1
            m+=1
        if dic1==dic2:
            return True
        left=0
        for ri in range(len(s1),len(s2)):
            dic2[s2[left]]-=1
            if dic2[s2[left]]==0:
                del dic2[s2[left]]
            dic2[s2[ri]]=dic2.get(s2[ri],0)+1
            if dic2==dic1:
                return True
            else:
                left+=1
        return False