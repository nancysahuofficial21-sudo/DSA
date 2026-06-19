class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt=0
        maxalt=0
        for g in gain:
            alt+=g
            maxalt=max(maxalt, alt)
        return maxalt
        