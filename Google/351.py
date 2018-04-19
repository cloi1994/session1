class Solution:
    """
    @param m: an integer
    @param n: an integer
    @return: the total number of unlock patterns of the Android lock screen
    """
    def numberOfPatterns(self, m, n):
        # Write your code here
        
        nums = [1,2,3,4,5,6,7,8,9]
        
        jumps = [ [0] * 10 for _ in range(10)]
        jumps[1][3] = jumps[3][1] = 1
        jumps[4][6] = jumps[6][4] = 4
        jumps[7][9] = jumps[9][7] = 7
        jumps[1][7] = jumps[7][1] = 3
        jumps[2][8] = jumps[8][2] = 4
        jumps[3][9] = jumps[9][3] = 5
        jumps[1][9] = jumps[9][1] = jumps[3][7] = jumps[7][3] = 4

        visited = [0] * len(nums) 
        self.res = 0
        self.dfs(m,n,nums,[],visited,jumps)
    
        return self.res
    def dfs(self,m,n,nums,tmp,visited,jumps):
        if len(tmp) >= m:
            #print tmp
            self.res += 1
        if len(tmp) >= n:
            return
        
        for i in range(len(nums)):
            if not tmp:
                jump  = 0
            else:
                jump = jumps[tmp[-1]][nums[i]]
            if tmp:
                print [tmp[-1], nums[i], visited[jump]]
                print jump
            if visited[i] == 0 and (jump == 0 or visited[jump] == 1):
                
                visited[i] = 1
                tmp.append(nums[i])
                self.dfs(m,n,nums,tmp,visited,jumps)
                visited[i] = 0
                tmp.pop()
