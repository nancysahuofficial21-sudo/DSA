class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       seen=[]
       for i in nums[::-1]:
        if i in seen:
            nums.remove(i)
        else:
            seen.append(i)
       return len(seen)
          