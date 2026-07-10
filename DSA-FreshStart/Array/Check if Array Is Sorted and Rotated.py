class Solution:
    def check(self, nums: List[int]) -> bool:
        drop=0
        for i in range(0,len(nums)):
            if(nums[i]>nums[(i+1)%len(nums)]): #modulo is used as it is a circular array so for the last elemnet,we will compare it with the first element
                drop+=1
        
        #if one drop is there -> rotate and sorted, zero drop -> array is fully sorted
        if(drop<=1):
            return True
        
        return False
