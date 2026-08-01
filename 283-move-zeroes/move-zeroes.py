class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i] , nums[insert]= nums[insert], nums[i]
                insert+=1
        return insert

        """
        Do not return anything, modify nums in-place instead.
        """
        