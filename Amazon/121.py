class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        
        gain = [0] * (len(prices) - 1)
        
        for i in range(1,len(prices)):
            gain[i-1] = prices[i] - prices[i-1]
        
        
        dp = [gain[0]] + [0] * (len(gain) - 1)
        
        for i in range(1,len(gain)):
            dp[i] = max(gain[i],dp[i-1]+gain[i])
            
        return max(0,max(dp))
        
