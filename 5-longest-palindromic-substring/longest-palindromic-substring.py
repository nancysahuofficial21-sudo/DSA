class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            # 1. Odd-length palindromes (single-character center)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
                
            # 2. Even-length palindromes (two-character center)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
                
        return res
