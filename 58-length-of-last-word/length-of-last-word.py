class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        res= s.split()
        count=len(res[-1])
        
        return count
    
                
        