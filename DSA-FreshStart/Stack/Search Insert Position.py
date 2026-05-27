class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=left + (right-left)//2
            if(nums[mid]==target):
                return mid
            elif(target<nums[mid]):
                right=mid-1
            else:
                left+=1
        
        #if mid index is not returned, then the correct position will be the left index
        return left
