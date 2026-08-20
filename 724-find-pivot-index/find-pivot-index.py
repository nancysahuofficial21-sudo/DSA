class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumleft=[]
        sumri=[]
        sumri.append(sum(nums[1:]))
        sumleft.append(0)
        for i in range(len(nums)-1):
            sumleft.append(sumleft[i]+nums[i])
        for k in range(1,len(nums)):
            sumri.append(sumri[k-1]-nums[k])

        print(sumleft)
        print(sumri)
        j=0
        while j<len(sumleft) and j<len(sumri):
            if sumleft[j]==sumri[j]:
                return j
            j+=1
       
        return -1
        