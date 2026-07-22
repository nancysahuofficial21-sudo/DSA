class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxstep=0
        for i, step in enumerate(nums):
            if i>maxstep:
                return False
            maxstep=max(maxstep,i+step)
            if maxstep>=len(nums)-1:
                return True
