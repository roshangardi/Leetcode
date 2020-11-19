from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit


sol = Solution()
stock_list = [2, 4, 1]
# stock_list = [7,1,5,3,6,4]
print(sol.maxProfit(stock_list))
