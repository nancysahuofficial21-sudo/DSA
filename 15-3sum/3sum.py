class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # If the current number is positive, we can never reach a sum of 0
            if nums[i] > 0:
                break
            
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Use two pointers for the remaining part of the array
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum < 0:
                    left += 1  # We need a larger sum
                elif three_sum > 0:
                    right -= 1 # We need a smaller sum
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicates for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res

        