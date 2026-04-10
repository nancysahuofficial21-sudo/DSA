class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            temp=target
            for i in range(len(nums)):
                if nums[i]<=target:
                    continue
                else:
                    nums[i] , target= target, nums[i]
                    break

            return nums.index(temp)