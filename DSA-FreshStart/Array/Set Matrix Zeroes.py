class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        row_tracker = [0]*r
        col_tracker = [0]*c

        #traverse the 2D matrix
        for i in range(0,r):
            for j in range(0,c):
                if(matrix[i][j]==0):
                    row_tracker[i]=-1
                    col_tracker[j]=-1
        
        #again traverse the 2D matrix
        for i in range(0,r):
            for j in range(0,c):
                #if any of the tracker index value is -1, then make value to 0 (matrix)
                if(row_tracker[i]==-1 or col_tracker[j]==-1):
                    matrix[i][j]=0
        
        return matrix
