import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b)
        }
        r=[]
        for i in tokens:
            if i in ops:
                a=r.pop()
                b=r.pop()
                res=ops[i](b,a)
                r.append(res)
            else:
                r.append(int(i))
        return r[0]
        