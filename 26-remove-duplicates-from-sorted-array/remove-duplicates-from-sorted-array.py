class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        lastnum=nums[0]
        j=1
        res=1
        for i in range(1,len(nums)):
            if nums[i]!=lastnum:
                res+=1
                lastnum=nums[i]
                nums[j]=nums[i]
                j+=1
        return res