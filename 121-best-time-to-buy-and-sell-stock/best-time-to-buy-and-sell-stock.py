class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            currentProfit = prices[r] - prices[l] 
            if prices[l] < prices[r]:
                max_profit =max(currentProfit,max_profit)
            else:
                l = r
            r += 1
        return max_profit