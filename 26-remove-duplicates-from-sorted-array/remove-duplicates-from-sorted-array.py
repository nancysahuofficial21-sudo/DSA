class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0 
        for i in range(1, len(nums)):
            if nums[i] != nums[res]:
                res += 1
                nums[res] = nums[i]
        return res + 1