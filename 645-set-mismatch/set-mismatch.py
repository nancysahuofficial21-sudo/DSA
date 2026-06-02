class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        import statistics 
        res=[]
        for i in range(1,len(nums)+1):
            if i  not in nums:
                res=[statistics.mode(nums),i]
                print(res)
            else:
                pass
                
        return res
        