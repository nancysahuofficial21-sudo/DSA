class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor < 0 and dividend>0:
            divisor=abs(divisor)
            result= (int(dividend/divisor)*(-1))
        else:
            result=int(dividend/divisor)    
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result