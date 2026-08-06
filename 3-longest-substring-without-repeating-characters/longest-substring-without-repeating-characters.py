class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        seen=set()
        ml=0
        for i in range(len(s)):
            if s[i] not in seen:
                seen.add(s[i])
                ml=max(ml,(i-l)+1)
            else:
                while s[i] in seen:
                    seen.remove(s[l])
                    l+=1
                seen.add(s[i]) 
                ml=max(ml,i-l+1)
        return ml     