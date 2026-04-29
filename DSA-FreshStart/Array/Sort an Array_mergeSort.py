class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0,len(nums)-1,nums)
    
    #divide
    def mergeSort(self,low,high,nums):
        if(low<high):
            mid=low+(high-low)//2
            self.mergeSort(low,mid,nums)
            self.mergeSort(mid+1,high,nums)
            self.merge(low,mid,high,nums)
        return nums
    
    #conquer
    def merge(self,low,mid,high,nums):
        n1 = mid-low+1
        n2 = high-mid

        arr1 = [0]*n1
        arr2 = [0]*n2

        #now insert values from nums to arr1 and arr2
        for i in range(0,n1):
            arr1[i]=nums[low+i]
        
        for i in range(0,n2):
            arr2[i]=nums[mid+i+1]
        
        #Now will traverse both the array and will insert in nums in ascending order
        k=low #this index will track the nums array
        i=0
        j=0
        while(i<n1 and j<n2):
            if(arr1[i]<=arr2[j]):
                nums[k]=arr1[i]
                i+=1
            else:
                nums[k]=arr2[j]
                j+=1
            k+=1
        
        while(i<n1):
            nums[k]=arr1[i]
            i+=1
            k+=1
        while(j<n2):
            nums[k]=arr2[j]
            j+=1
            k+=1   
