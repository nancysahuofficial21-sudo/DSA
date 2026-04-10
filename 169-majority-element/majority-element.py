class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        for i in nums:
            seen[i]= seen.get(i,0)+1
        for key in seen:
            if seen[key]>len(nums)//2:
                return key        

        