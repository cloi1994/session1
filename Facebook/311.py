class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        
        res = [ [0 for i in range(len(B[0]))] for j in range(len(A))]
        
        rowA = [False] * len(A) 
        rowB = [False] * len(B[0])
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    rowA[i] = True
                    break
             
        # Swap i,j     
        for j in range(len(B[0])):
            for i in range(len(B)):
                if B[i][j] != 0:
                    rowB[j] = True
                    break
                
        for i in range(len(A)):
            for j in range(len(B[0])):
                if not rowA[i] or not rowB[j]:
                    res[i][j] = 0
                    continue
                summ = 0
                
                for k in range(len(A[0])):
                    summ += A[i][k] * B[k][j]
                
                res[i][j] = summ
                
        return res
        
        
        
