class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        dic=0
        maxlen=0
        for ri in range(len(nums)):
            if nums[ri]==0:
                dic+=1
            while dic>k:
                if  nums[left]==0:
                    dic-=1
                left+=1
            maxlen=max(maxlen, ri-left+1)
        return maxlen
    