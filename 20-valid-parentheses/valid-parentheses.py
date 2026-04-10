class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        p={")":"(",
           "]":"[",
           "}":"{"
        }
        for i in list(s):
            if stack:
                if p.get(i)== stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return not stack                  


        