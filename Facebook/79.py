class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        visted = [ [ 0 for m in range(len(board[0]))] for n in range(len(board))]

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(0,visted,board,word,i,j):
                    return True
                
        return False
    
    
    def dfs(self,index,visted,board,word,i,j):
        
        if index == len(word):
            return True
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visted[i][j] or word[index] != board[i][j]:
            return False        
        
        visted[i][j] = 1
        
        exist = self.dfs(index+1,visted,board,word,i+1,j) or self.dfs(index+1,visted,board,word,i,j+1) or self.dfs(index+1,visted,board,word,i-1,j) or self.dfs(index+1,visted,board,word,i,j-1)
        
        visted[i][j] = 0
        
        return exist
        
