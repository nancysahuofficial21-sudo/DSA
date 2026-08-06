class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sas=sum(nums[:k])
        currentavg=sas/k
        
        maxavg=currentavg
        i=0
        while i+k<len(nums):
            sas=sas-nums[i]+nums[i+k]
            currentavg=sas/k
            
            maxavg=max(maxavg, currentavg)
            i+=1
        return maxavg
        