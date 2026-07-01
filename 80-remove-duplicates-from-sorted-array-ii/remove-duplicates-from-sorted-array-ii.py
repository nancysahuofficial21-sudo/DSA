class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        i=2
        j=2
        while i<len(nums):
            if nums[i]!=nums[j-2]:
                nums[j]=nums[i]
                j+=1
            i+=1
        return j
            