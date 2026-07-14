class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefixSum=0
        hashMap={}
        maxSize=0
        for i in range(0,len(arr)):
            prefixSum+=arr[i]
            
            if(prefixSum==k):
                size = i+1
                maxSize = max(maxSize,size)
            
            rem = prefixSum-k
            #check if rem is there in the hashmap
            if(rem in hashMap):
                size = i-hashMap[rem]
                maxSize=max(maxSize,size)
            
            #if the prefix Sum is not in hasmap then only add it, otherwise it will update the index and it store smallest subarray with sum k
            if(prefixSum not in hashMap):
                hashMap[prefixSum]=i
        
        return maxSize
