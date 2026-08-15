class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        minlen=float('inf')
        currsum=0
        for ri in range(len(nums)):
            currsum+=nums[ri]
            while currsum>=target:
                minlen=min(minlen, ri-left+1)
                currsum-=nums[left]
                left+=1
        return 0 if minlen==float('inf') else minlen

        