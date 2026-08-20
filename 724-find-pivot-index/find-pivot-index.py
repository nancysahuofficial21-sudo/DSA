class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumleft=[]
        sumri=[]
        for i in range(len(nums)):
            sumleft.append(sum(nums[:i]))
            sumri.append(sum(nums[i+1:]))
        j=0
        while j<len(sumleft) and j<len(sumri):
            if sumleft[j]==sumri[j]:
                return j
            j+=1
        print(sumleft)
        print(sumri)
        return -1
        