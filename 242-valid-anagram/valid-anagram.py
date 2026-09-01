class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        l=list(s)
        k=list(t)
        l.sort()
        k.sort()
        for i in range(len(s)):
            if l[i]!=k[i]:
                return False
        return True