class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ind=[-1,-1]
        for i in range(2):
            l=0
            r=len(nums)-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    ind[i]=mid  
                    if i==0:
                        r=mid-1
                    else:
                        l=mid+1                  
                elif nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
        
        return ind