class Solution:
    def leaders(self, arr):
        # code here
        
        # Optimized approach
        result=[]
        maxi=arr[len(arr)-1]  #current maximum element will be the last element.
        
        #rightmost element will always be the leader
        result.append(maxi)
        
        #traverse from the back of the array (second last element)
        for i in range(len(arr)-2,-1,-1):
            if(arr[i]>=maxi):
                maxi=arr[i]
                result.append(maxi)
        
        #now i have the result array but it is in reverse order
        result.reverse()
        return result
