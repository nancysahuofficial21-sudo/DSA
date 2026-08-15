class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        dic={}
        maxlen=0
        for ri in range(len(nums)):
            dic[nums[ri]]=dic.get(nums[ri],0)+1
            while nums[ri]==0 and dic[nums[ri]]>k:
                dic[nums[left]]-=1
                left+=1
            maxlen=max(maxlen, ri-left+1)
        return maxlen
    