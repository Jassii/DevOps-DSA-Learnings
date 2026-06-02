class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Brute force approach
        # for i in range(0,len(matrix)):
        #     for j in range(0,len(matrix[0])):
        #         if(matrix[i][j]==target):
        #             return True
        # return False

        #Better approach
        #find the row
        # row=-1
        # for i in range(0,len(matrix)):
        #     arr=matrix[i]
        #     #it will help in deciding the row, without going to each row.
        #     if(target>=arr[0] and target<=arr[len(arr)-1]):
        #         start=0
        #         end=len(arr)-1
        #         while(start<=end):
        #             mid=start+(end-start)//2
        #             if(arr[mid]==target):
        #                 return True
        #             elif(arr[mid]<target):
        #                 start=mid+1
        #             else:
        #                 end=mid-1
        # return False



        #Optimized Approach
        #find the row using binary search - o(log n)
        rows=len(matrix)
        col=len(matrix[0])
        top=0
        bot=rows-1
        #finding the row which can contain the target
        while(top<=bot):
            row=top+(bot-top)//2
            if(target>matrix[row][-1]):
                top=row+1
            elif(target<matrix[row][0]):
                bot=row-1
            else:
                break
        
        #now the row will contain that value that may or may not contain the target
        #O(log m)
        start=0
        end=len(matrix[row])-1
        while(start<=end):
            mid=start+(end-start)//2
            if(target==matrix[row][mid]):
                return True
            elif(target<matrix[row][mid]):
                end=mid-1
            else:
                start=mid+1
        return False

        #At last total complexity is O(log n) + O(log m) i.e. O(log(m*n))
