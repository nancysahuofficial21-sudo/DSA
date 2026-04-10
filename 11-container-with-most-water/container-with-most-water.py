class Solution:
    def maxArea(self, height: List[int]) -> int:
        a= 0
        b= len(height)-1
        maxarea=0
        while a<b:
            maxarea= max(maxarea, (b-a) * min(height[a], height[b]))
            if height[a]<height[b]:
                a+=1
            else:
                b-=1
        return maxarea     
                       
        