class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force approach:
        #TC - O(n^2)
        # longest = 0
        # for i in range(0,len(nums)):
        #     count = 1
        #     value = nums[i]
        #     j = 0
        #     while(j<len(nums)):
        #         if(nums[j]==value+1):
        #             count+=1
        #             value+=1
        #             j=0 #for new value it should start checking from the 0th index element
        #         else:
        #             j+=1
        #     #value+1 is not found throughout the array
        #     longest = max(count,longest)

        # return longest


        #Optimized Approach
        
        #if the length of the array is 1
        if(len(nums)==0 or len(nums)==1):
            return len(nums)

        #first sort the array
        nums.sort()

        longest=1 #one number can be the longest sequence of the list
        count=1
        for i in range(0,len(nums)-1):
            if(nums[i]==nums[i+1]):
                continue
            elif(nums[i]+1==nums[i+1]):
                count+=1
                longest=max(longest,count)
            else:
                longest=max(longest,count)
                count=1
        return longest
