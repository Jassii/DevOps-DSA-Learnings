class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #brute force approach
    #     r = len(matrix)
    #     c = len(matrix[0])

    #     #taking a new 2D matrix that will store the transpose of the above matrix
    #     #initialize the matrix with the value 0 and transpose size.
    #     tp = [[0]*r for _ in range(0,c)]


    #     for i in range(0,r):
    #         for j in range(0,c):
    #             tp[j][i] = matrix[i][j]
    #     #now i have the transpose of the matrix

    #     #now traverse the transpose and reverse each row
    #     for i in range(0,len(tp)):
    #         arr = tp[i] #each row list
    #         #now reverse it
    #         self.reverse(0,len(arr)-1,arr)
        
        
    #     #now put all the values of tp matrix into main matrix
    #     for i in range(0,r):
    #         for j in range(0,c):
    #             matrix[i][j] = tp[i][j]
        

    # #function to reverse the list
    # def reverse(self,l,r,arr):
    #     while(l<r):
    #         arr[l],arr[r]=arr[r],arr[l]
    #         l+=1
    #         r-=1

    #optimized approach

        r = len(matrix)
        c = len(matrix[0])

        #transpose of the matrix in place
        for i in range(0,r):
            for j in range(i,c):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j] #swap it
    
        #now traverse each row and reverse it
        for i in range(0,r):
            arr = matrix[i]
            self.reverse(arr,0,len(arr)-1)
    

    def reverse(self,arr,l,r):
        while(l<r):
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
