class Solution:
    def findFloor(self, arr, x):
        # code here
        return self.search(0,len(arr)-1,arr,x)
    
    #here I will find the index for the element that is less than equal to x
    def search(self,start,end,arr,x):
        ans=-1
        while(start<=end):
            mid=start+(end-start)//2
            if(arr[mid]<=x):
                ans=mid
                start=mid+1
            elif(arr[mid]>x):
                end=mid-1
        return ans
