class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #brute force approach -> O(n^2)
        # max_count=0
        # for i in range(0,len(nums)):
        #     num=nums[i]
        #     count=1
        #     while num+1 in nums:
        #         count+=1
        #         num+=1
        #     max_count=max(max_count,count)
        # return max_count


        #Optimized Approach

        #sort the array
        nums.sort()
        max_count=0
        last_smaller=float("-inf")
        count=0
        for i in range(0,len(nums)):
            value=nums[i]
            if(value-1==last_smaller):
                count+=1
            elif(value==last_smaller):
                continue
            else:
                count=1
                
            max_count=max(max_count,count)
            last_smaller=nums[i]
        return max_count
