import sys
class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        
        # kadane's algorithm
        currSum=0
        maxSum=-sys.maxsize-1.  #smallest value
        for i in range(0,len(arr)):
            currSum = max(arr[i],currSum+arr[i])
            maxSum = max(maxSum,currSum
        
        return maxSum
        
        
        
        #when there is a need to get the subarray
        #when there is a need to get the subarray.
        # arrStart=-1 #starting index
        # arrEnd=-1 #ending index
        # maxSum=-sys.maxsize-1
        # currSum=0
        # for i in range(0,len(arr)):
        #     #if currSum==0, its index can be the starting point
        #     if(currSum==0):
        #         start=i
                
        #     currSum+=arr[i]
        #     if(currSum>maxSum):
        #         maxSum=currSum
        #         arrStart=start #starting index
        #         arrEnd=i #ending index
                
        #     #if currSum is less than 0, then assign it as 0
        #     if(currSum<0):
        #         currSum=0
            
            
        
        
        #brute force approach, taking out all subarrays and taking out its sum
        # maxSum = -sys.maxsize-1
        # for i in range(0,len(arr)):
        #     for j in range(i,len(arr)):
        #         total=0
        #         for k in range(i,j+1):
        #             total += arr[k]
        #         maxSum=max(maxSum,total)
        # return maxSum          
        
        
