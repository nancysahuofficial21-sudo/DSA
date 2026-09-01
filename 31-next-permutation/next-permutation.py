class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        t=False
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                t=True
                j=len(nums)-1
                while nums[j]<=nums[i]:
                    j-=1
                nums[j],nums[i]=nums[i],nums[j]
                nums[i+1:]=nums[i+1:][::-1]
                break
        if not t:
            nums.reverse()
                