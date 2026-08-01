class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cun=nums[0]
        i=1
        count=1
        for j in range(1,len(nums)):
            print(nums[j],nums[i])
            if nums[j]!=cun:
                nums[j], nums[i]= nums[i], nums[j]
                cun=nums[i]
                count+=1
                i+=1
        return count




        