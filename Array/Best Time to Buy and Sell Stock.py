class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > min_price:
                profit = prices[i] - min_price
                if profit > result:
                    result = profit
            else:
                min_price = prices[i]
        return result


prices = [7, 1, 5, 3, 6, 4]
obj = Solution()
result = obj.maxProfit(prices)
print(result)
