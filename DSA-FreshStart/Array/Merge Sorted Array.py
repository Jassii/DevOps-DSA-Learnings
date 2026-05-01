class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        #Optimized approach without using any space complexity O(1)
        #insert from the end (max element at last)
        k=len(nums1)-1
        i=m-1
        j=n-1
        while(i>=0 and j>=0):
            if(nums1[i]>=nums2[j]):
                nums1[k]=nums1[i]
                i-=1
            else:
                nums1[k]=nums2[j]
                j-=1
            k-=1
        
        #if any array elements are still there
        while(i>=0):
            nums1[k]=nums1[i]
            i-=1
            k-=1

        while(j>=0):
            nums1[k]=nums2[j]
            j-=1
            k-=1
        


        #Brute force approach (here space complexity is O(n))
        # i=0
        # j=0
        # res=[]
        # while(i<m and j<n):
        #     if(nums1[i]<=nums2[j]):
        #         res.append(nums1[i])
        #         i+=1
        #     else:
        #         res.append(nums2[j])
        #         j+=1
        
        # while(i<m):
        #     res.append(nums1[i])
        #     i+=1
        # while(j<n):
        #     res.append(nums2[j])
        #     j+=1
        
        # #put all the elements in res into nums1
        # for i in range(0,len(res)):
        #     nums1[i]=res[i]
