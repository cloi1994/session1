class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        n = len(nums)
        prefix_sum = [0] * (n+1)
        
        best = float('-inf')
        
        for x in range(1,n+1):
            prefix_sum[x] = prefix_sum[x-1] + nums[x-1]
            
        for i in range(n+1):
            for j in range(n+1):
                if prefix_sum[j] - prefix_sum[i] == k:
                    best = max(best,j-i)
                    
        return best
