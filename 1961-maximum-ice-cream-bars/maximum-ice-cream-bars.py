class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_val = max(costs)
        count = [0] * (max_val + 1)
        output = [0] * len(costs)

        for num in costs:
            count[num] += 1

        for i in range(1, len(count)):
            count[i] += count[i - 1]

        for num in reversed(costs):
            output[count[num] - 1] = num
            count[num] -= 1

        for i in range(len(costs)):
            costs[i] = output[i]
        print(costs)
        res=0

        for i in costs:
            if coins-i>0 or coins-i==0:
                res+=1
                coins=coins-i
                print(coins)
        return res

        
        