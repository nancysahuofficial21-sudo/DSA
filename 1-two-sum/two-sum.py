class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seennum={}
        for i, n in enumerate(nums):
            diff=target-n
            if diff not in seennum:
                seennum[n]=i
            else:
                return [seennum[diff],i]    
