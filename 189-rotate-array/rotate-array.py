class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        #op=[0]*len(nums)
        i=0
        stagedElement=None
        visitedCount=0
        while(visitedCount!=len(nums)):
            start=i
            while(True):
                nextElement=(i+k)%(len(nums))
                if(stagedElement==None):
                    x=nums[nextElement]
                    nums[nextElement]=nums[i]
                    stagedElement=x
                else:
                    x=nums[nextElement]
                    nums[nextElement]=stagedElement
                    stagedElement=x
                visitedCount=visitedCount+1
                i=nextElement
                print(stagedElement)
                if(i==start):
                    i=i+1
                    stagedElement=None
                    break
            
            
