class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        
        #k 
        #arr = [7, 1, 5, 3, 6, 4]
        #k =   [   -6, 4, -2, 3, -2]  min of i-1
        #       max(-6 4  2  5  3)
        gain = []
        for i in range(1,len(prices)):
            gain.append(prices[i]-prices[i-1])
        
        dp = [0] * len(gain)
        
        
        dp[0] = gain[0]
        ans = gain[0]
        
        for i in range(1,len(gain)):
            dp[i] = max(dp[i-1] + gain[i] , gain[i])
            ans = max(ans,dp[i])
        
        return max(0,ans)
            
        
