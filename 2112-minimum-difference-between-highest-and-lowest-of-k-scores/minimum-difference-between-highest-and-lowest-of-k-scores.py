class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        print(nums)
        
        if len(nums)==1:
            return 0
        else:
            mindif=nums[-1]
            for i in range(len(nums)-k+1):
                mindif=min(mindif, (nums[i+k-1] - nums[i]))
                print(nums[i+k-1],nums[i],mindif)
        return mindif

        