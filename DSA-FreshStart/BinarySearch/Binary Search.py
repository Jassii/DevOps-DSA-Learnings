class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        return self.binarySearch(start,end,nums,target)
    
    def binarySearch(self,start,end,nums,target):
        while(start<=end):
            mid = start + (end-start)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]<target):
                start=mid+1
            else:
                end=mid-1
        
        #if nothing is found then
        return -1
