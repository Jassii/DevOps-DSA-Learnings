class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        
        #first take out the sum from i=0 to k-1
        summ = 0
        for i in range(0,k):
            summ+=nums[i]

        #now for the first k elements, even it is less than k, the max avg will be
        maxAvg = summ/k

        l=0 #left
        r=k-1 #right 
        maxSum=summ #maxsum as of now

        #calculate max sum in the fixed length of the array size k
        while(r<n-1):
            summ -= nums[l]
            l+=1
            r+=1
            summ += nums[r]
            maxSum = max(maxSum,summ)
        
        #calculate the avg of the max sum, that will be maxavg.
        maxAvg = maxSum/k
        return maxAvg
