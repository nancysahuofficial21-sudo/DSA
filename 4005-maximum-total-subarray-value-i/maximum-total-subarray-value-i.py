class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        maxe=max(nums)
        mine=min(nums)
        sumn=0
        for i in range(k):
            sumn+=maxe-mine
        return sumn


        