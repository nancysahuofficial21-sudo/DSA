class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di={}
        for i in nums:
            di[i]=di.get(i,0)+1
        dis= sorted(di.items(),key= lambda x: x[1], reverse=True)
        res=[]
        for i in dis[:k]:
            res.append(i[0])
        return res