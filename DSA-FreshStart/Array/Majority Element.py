class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #brute force approach
        # hmap={}
        # for i in range(0,len(nums)):
        #     hmap[nums[i]] = hmap.get(nums[i],0)+1
        
        # for key,value in hmap.items():
        #     if(value>len(nums)//2):
        #         return key

        
        #optimized approach
        #Moore's Voting Algorithm
        element=nums[0]
        count=0
        for i in range(0,len(nums)):
            if(nums[i]==element):
                count+=1
            else:
                count-=1
                if(count==0):
                    element=nums[i+1]
        
        #now this element can be the majority element but to be sure, we need to check the count
        count=0
        for i in range(0,len(nums)):
            if(nums[i]==element):
                count+=1
        if(count>len(nums)//2):
            return element
