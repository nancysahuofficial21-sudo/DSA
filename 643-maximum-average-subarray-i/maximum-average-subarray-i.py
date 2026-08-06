class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sas=sum(nums[:k])
        maxavg=sas
        i=0
        while i+k<len(nums):
            sas=sas-nums[i]+nums[i+k]
            if sas>maxavg:
                maxavg=sas
            i+=1
        return maxavg/k
        