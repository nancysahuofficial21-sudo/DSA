class Solution:
    def isPalindrome(self, x: int) -> bool:
        result= False 
        if x<0 :
            result= False
        else:
            l1= list(str(x))
            if l1==l1[::-1]:
                result= True  
            else:
                result= False
        return result        