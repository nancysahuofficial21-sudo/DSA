class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod=1
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=lprod
            lprod*=nums[i]
        rprod=1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=rprod
            rprod*=nums[j]
        return res
        