class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        def rev(i,j):
            while i<j:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j-=1
        rev(0,n-1)
        rev(0,k-1)
        rev(k,n-1)

        """
        Do not return anything, modify nums in-place instead.
        """
        