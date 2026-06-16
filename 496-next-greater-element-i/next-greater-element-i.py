class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans={}
        res=[]
        for i in reversed(nums2):
            while stack and stack[-1] < i:
                stack.pop()
            ans[i]=stack[-1] if stack else -1
            stack.append(i)
        return [ans[i] for i in nums1]    
    
        