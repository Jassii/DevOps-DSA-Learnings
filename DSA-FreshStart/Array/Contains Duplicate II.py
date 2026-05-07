class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Optimized approach
        #using hashmap
        hmap={}
        for i in range(0,len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]]=i
            else:
                if(abs(hmap[nums[i]]-i)<=k):
                    return True
                else:
                    hmap[nums[i]]=i
        return False
        
        #Brute force approach
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]==nums[j] and abs(i-j)<=k):
        #             return True
        # return False
