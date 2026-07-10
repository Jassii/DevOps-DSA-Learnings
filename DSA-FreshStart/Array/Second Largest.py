class Solution:
    def getSecondLargest(self, arr):
        # code here
        #Brute force approach - O(2n)
        # maxi=arr[0]
        # for i in range(0,len(arr)):
        #     if(arr[i]>maxi):
        #         maxi=arr[i]
        # #now i have the maximum element
        
        # sec_maxi=-1
        # for i in range(0,len(arr)):
        #     if(arr[i]>sec_maxi and arr[i]<maxi):
        #         sec_maxi=arr[i]
        # return sec_maxi
        
        #Optimized Approach - O(n)
        sec_max=-1
        maxi=arr[0]
        for i in range(1,len(arr)):
            if(arr[i]>maxi):
                sec_max=maxi
                maxi=arr[i]
            elif(arr[i]<maxi):
                if(arr[i]>sec_max):
                    sec_max=arr[i]
        return sec_max
