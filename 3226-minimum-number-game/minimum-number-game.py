class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=[]
        while nums:
            a=nums.pop(nums.index(min(nums)))
            b=nums.pop(nums.index(min(nums)))
            res.append(b)
            res.append(a)
        return res

        