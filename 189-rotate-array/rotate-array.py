class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        """
        n=len(nums)
        k=k%n
        def reverse(start,end):
            while start<end:
                nums[start], nums[end]= nums[end], nums[start]
                start += 1  # Moves the left pointer RIGHT (increases index)
                end -= 1    # Moves the right pointer LEFT (decreases index)
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
            
            
