class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        minlen=float('inf')
        currlen=0
        currsum=0
        for ri in range(len(nums)):
            currsum+=nums[ri]
            currlen+=1
            while currsum>=target:
                minlen=min(minlen, currlen)
                currsum-=nums[left]
                currlen-=1
                left+=1
            
        return 0 if minlen==float('inf') else minlen

        