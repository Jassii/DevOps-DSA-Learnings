class Solution:
    def majorityElement(self, arr):
        #code here
        
        #Brute force approach
        #usage of hashmap. TC - O(n)
        # SC - O(n)
        # n=len(arr)
        # count_map={}
        # for i in range(0,len(arr)):
        #     if(arr[i] in count_map):
        #         count_map[arr[i]]+=1
        #     else:
        #         count_map[arr[i]]=1
        
        
        # #now traverse count_map
        # for key,value in count_map.items():
        #     if(value>n//2):
        #         return key
        
        # #if the majority element doen not exists
        # return -1
        
        
        
        #Optimized approach 
        element=-1
        count=0
        #traverse the array
        for i in range(0,len(arr)):
            if(count==0):#if the count is zero, update element and make count to 1
                element=arr[i]
                count=1
            elif(arr[i]==element): #if the element matches, increase the count by 1
                count+=1
            else:#if the element is not same, decrease the count by 1
                count-=1
            
        #verify if the element if the majority element or not.
        count=0
        for i in range(0,len(arr)):
            if(arr[i]==element):
                count+=1
        
        #if the count of the element if greater than n/2, then it is the majority element
        if(count>len(arr)//2):
            return element
            
        return -1
        
