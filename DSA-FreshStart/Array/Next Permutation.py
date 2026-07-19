class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #find the break point
        bp=-1
        for i in range(0,len(nums)-1):
            if(nums[i]<nums[i+1]):
                bp=i
        
        #there is no break point(last subarray) then return the first subarray
        if(bp==-1):
            return self.reverse(0,len(nums)-1,nums)
        
        #now there is a break point at index i
        for i in range(len(nums)-1,bp,-1):
            if(nums[i]>nums[bp]):
                #swap it
                nums[i],nums[bp]=nums[bp],nums[i]
                break

        #now reverse to get the minimum next permutation 
        self.reverse(bp+1,len(nums)-1,nums)

        #at the end return the updated array
        return nums

    def reverse(self,start,end,nums):
        while(start<end):
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
