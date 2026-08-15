class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic={}
        left=0
        maxlen=-float('inf')
        for ri in range(len(fruits)):
            dic[fruits[ri]]= dic.get(fruits[ri],0)+1
            while len(dic)>2:
                dic[fruits[left]]-=1
                if dic[fruits[left]]==0:
                    del dic[fruits[left]]
                left+=1
            maxlen=max(maxlen, ri-left+1)
            
        return len(fruits) if maxlen==-float('inf') else maxlen
        
