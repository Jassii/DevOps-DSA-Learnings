class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #using hashset
        seen = set()
        for i in range(0,len(nums)):
            value=nums[i]
            if value not in seen:
                seen.add(value)
            else:
                return True
        return False



        #using dictionary
        # hmap=dict()
        # for i in range(0,len(nums)):
        #     value=nums[i]
        #     hmap[value]=hmap.get(value,0)+1
        

        # for key,value in hmap.items():
        #     if(value>=2):
        #         return True

        # return False

        #Brute force approach
        # res=[]
        # for i in range(0,len(nums)):
        #     value=nums[i]
        #     if(value not in res):
        #         res.append(value)
        #     else:
        #         return True
        # return False
