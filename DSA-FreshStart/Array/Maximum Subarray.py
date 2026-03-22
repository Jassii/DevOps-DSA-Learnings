class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
      
        #brute force approach - O(n^3)
        max_sum=0
        if(len(nums)==1):
            if(nums[0]>0):
                return nums[0]

        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                curr_sum=0
                for k in range(i,j+1):
                    curr_sum+=nums[k]
                max_sum=max(max_sum,curr_sum)
        return max_sum


        #optimized approach - Kadane's Algorithm -> O(n)
        # curr_sum=0
        # max_sum=0
        # for i in range(0,len(nums)):
        #     curr_sum=max(nums[i],curr_sum+nums[i])
        #     max_sum=max(max_sum,curr_sum)
        # return max_sum
