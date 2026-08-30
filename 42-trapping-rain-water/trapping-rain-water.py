class Solution:
    def trap(self, height: List[int]) -> int:
        i=1
        j=len(height)-2
        leftmax=[height[0]]
        rightmax=[height[len(height)-1]]
        while i<len(height):
            if height[i]>leftmax[i-1]:
                leftmax.append(height[i])
            else:
                leftmax.append(leftmax[i-1])
            if height[j]>rightmax[i-1]:
                rightmax.append(height[j])
            else:
                rightmax.append(rightmax[i-1])
            j-=1
            i+=1
        rightmax.sort(reverse=True)
        wateratk=0
        for k in range(len(height)):
            wateratk+=min(leftmax[k],rightmax[k])-height[k]
        return wateratk

                
            