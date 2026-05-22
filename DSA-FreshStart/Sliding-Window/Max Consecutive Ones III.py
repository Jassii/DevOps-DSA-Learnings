class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #find the maximum length subarray with atmost k zeros
        
        #brute force approach
        # maxL=0
        # for i in range(0,len(nums)):
        #     for j in range(i,len(nums)):
        #         count=0
        #         for t in range(i,j+1):
        #             if(nums[t]==0):
        #                 count+=1
        #         if(count<=k):
        #             maxL=max(maxL,j-i+1)
        # return maxL

        #optimized approach
        # i=0
        # j=0
        # maxL=0
        # count=0
        # while(j<len(nums)):
        #     if(nums[j]==0):
        #         count+=1
        #         if(count<=k):
        #             j+=1
        #         else:
        #             maxL=max(maxL,j-i)
        #             while(nums[i]!=0):
        #                 i+=1
        #             i+=1
        #             count-=2
        #     else:
        #         j+=1
        # maxL = max(maxL,j-i)
        
        # return maxL


        #more good written code
        l=0
        r=0
        count=0
        maxL=0
        while(r<len(nums)):
            if(nums[r]!=0):
                maxL=max(maxL,r-l+1)
                r+=1
            else:
                count+=1
                if(count<=k):
                    maxL=max(maxL,r-l+1)
                    r+=1
                else:
                    while(nums[l]!=0):
                        l+=1
                    count-=1
                    l+=1
                    maxL=max(maxL,r-l+1)
                    r+=1
        return maxL
