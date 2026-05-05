class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #Optimized Approach -> O(nlogn)+O(n^2) -> O(n^2)

        #first sort the array for skipping repeated elements
        nums.sort()
        res = []
        
        for i,a in enumerate(nums):
            #skip this condition for the 0th index, as here both will be same, we are doing this 
            #to avid the repeation #if the value already has come, then skip that value
            if(i>0 and a==nums[i-1]):
                continue

            #now perform the two sum strategy and notice that the array is sorted (two pointer aproach)
            l = i + 1
            r = len(nums) - 1
            while(l<r):
                threeSum = a + nums[l] + nums[r]
                if(threeSum > 0):
                    r-=1
                elif(threeSum < 0):
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    #but suppose the next l, also has the same value which old s had
                    #so move it untill it is different but also make sure that l does not cross r
                    while(nums[l]==nums[l-1] and l<r):
                        l+=1

        return res



        #Brute force approach -> O(n^3)
        # res=[]
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         lis=[]
        #         for k in range(j+1,len(nums)):
        #             if(nums[i]+nums[j]+nums[k]==0):
        #                 lis.append(nums[i])
        #                 lis.append(nums[j])
        #                 lis.append(nums[k])
        #                 lis=sorted(lis)
        #                 if(lis not in res):
        #                     res.append(lis)
        #             lis=[]#making it empty
        # return res
