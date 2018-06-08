class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(numbers)):
            n = target - numbers[i]
            
            low = i + 1
            high = len(numbers) - 1
            
            while low <= high:
                mid = low + (high - low) / 2
                if numbers[mid] == n:
                    return [i+1,mid+1]
                if numbers[mid] > n:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
                    
