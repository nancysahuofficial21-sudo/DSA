class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1:
            return intervals
        intervals.sort()   
        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1]>intervals[i][0] and res[-1][1]>intervals[i][1]:
                pass
            elif res[-1][1]>=intervals[i][0]:
                res[-1][1]=intervals[i][1]
            else:
                res.append(intervals[i])
        return res