class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    k=stack.pop()
                    print(k)
                    continue
                elif stack[-1] == -a:
                    print(stack.pop())
                break
            else:
                stack.append(a)
        return stack