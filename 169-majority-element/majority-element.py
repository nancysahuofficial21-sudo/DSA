from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen=defaultdict(int)
        for num in nums:
            seen[num]+=1
        for key in seen:
            if seen[key]>len(nums)//2:
                return key