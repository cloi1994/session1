class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row, col check 
        for i in range(len(board)):
            rowset = set()
            for j in range(len(board[0])):
                num =  board[i][j]
                if num != '.':
                    if num in rowset:
                        return False
                    else:
                        rowset.add(num)
        for i in range(len(board)):
            colset = set()
            for j in range(len(board[0])):
                num =  board[j][i]
                if num != '.':
                    if num in colset:
                        return False
                    else:
                        colset.add(num)
                        
        for i in range(len(board)):
            boxset = set()
            for j in range(len(board[0])):
                rowIndex = 3 * (i/3 ) 
                colIndex = 3 * (i % 3)
                
                num = board[rowIndex + j/3][colIndex + j%3]
                
                if num != '.':
                    if num in boxset:
                        return False
                    else:
                        boxset.add(num)
        return True
    
        # i/3  ex : 0 , 0 , 0 , 1 ,1 , 1 , 2 , 2 , 2
        # i%3  ex: 0,1,2,0,1,2 ....
        # i*3 move to next block
        
