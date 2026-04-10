class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lp=""
        zipped=list(zip(*strs))
        for i in zip(*strs):
            if len(set(i))==1:
                lp=lp+i[0]
            else:
                break    
       
        return lp      

        