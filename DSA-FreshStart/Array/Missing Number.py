class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      #same number zor is 0, any number xor with 0 is the number
        ans=0
        for i in range(0,len(nums)):
            ans=ans^nums[i]
        
        for i in range(1,len(nums)+1):
            ans=ans^i
        
        return ans
