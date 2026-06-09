class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=set()
        c= []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                c=[nums.index(complement),i]

            seen.add(nums[i])
        return c 