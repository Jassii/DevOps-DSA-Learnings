class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        map=dict()
        for i in range(0,len(nums)):
            value = target-nums[i]
            if(value in map):
                res.append(map.get(value))
                res.append(i)
                return res
            else:
                map[nums[i]]=i
