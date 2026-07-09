class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Brute force approach ~ O(n^3)
        # count=0
        # for i in range(0,len(nums)):
        #     for j in range(i,len(nums)):
        #         summ=0
        #         for t in range(i,j+1):
        #             summ+=nums[t]
        #         if(summ==k):
        #             count+=1
        # return count

        #Better Approach Approach - O(n^2)
        #Here you dont need the third loop.
        # count=0
        # for i in range(0,len(nums)):
        #     summ=0
        #     for j in range(i,len(nums)):
        #         summ+=nums[j]
        #         if(summ==k):
        #             count+=1
        # return count

        #Optimized Approach - Prefix Sum
        prefixSum=0
        count=0
        hashmap={} #it will maintain prefixSum value with count
        
        #insert prefixSum with value 0 - inorder to handle (prefixSum-k) equals 0
        hashmap[0]=1
        
        for i in range(0,len(nums)):
            prefixSum+=nums[i]
            remove = prefixSum - k
            if(remove in hashmap):
                #how many times the prefix sum has came, so get the count
                count+=hashmap[remove]
            #if prefixSum is in hashmap, then increase its count by 1  
            # if(prefixSum in hashmap):
            #     hashmap[prefixSum] = hashmap.get(prefixSum)+1
            # else:
            #     hashmap[prefixSum] = 1 
            hashmap[prefixSum] = hashmap.get(prefixSum,0)+1   

        return count
