class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum= float('-inf')
        current=0
        if len(nums)==1:
            return nums[0]
        for i in nums:
            current=current+i
            if current>maxsum:
                maxsum=current
            if current<0:
                current=0
           
        return maxsum

        

        
        