class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<1:
            return len(nums)
        nums1=set(nums)
        ml=1
        for i in nums1:
            if i-1 not in nums1:
                l=1
                while i+1 in nums1:
                    i+=1
                    l+=1
                ml=max(ml,l)
        return ml