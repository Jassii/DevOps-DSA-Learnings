class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in range(0,len(nums)):
            ans=ans^nums[i] #XOR of the same gives zero, at last single number will exist (xor of number with 0, is that number)
        return ans
