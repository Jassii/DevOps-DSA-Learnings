class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        top=0
        left=0
        right=len(matrix[0])-1
        bottom=len(matrix)-1

        while(top<=bottom and left<=right):
            #now print right
            for i in range(left,right+1):
                res.append(matrix[top][i])
        
            #now print bottom
            top+=1
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
        
            #now print left
            right-=1
            #here we have to make a check, if its a single row, and n columns, it would have traversed
            #in the right movement
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
        
            #now print top
            bottom-=1
            #here we have to make a check, if it's single column and n rows, it would have traversed
            #in the down movement
            if(left<=right):
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
        
            left+=1

        return res
