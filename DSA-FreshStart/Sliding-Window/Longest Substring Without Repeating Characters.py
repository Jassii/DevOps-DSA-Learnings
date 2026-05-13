class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Optimized Approach - Sliding window approach
        sub=[]
        i=0
        j=0
        maxLen=0
        while(j<len(s)):
            if(s[j] not in sub):
                sub.append(s[j])
                maxLen=max(maxLen,j-i+1)
                j+=1
            while((j<len(s)) and (s[j] in sub)):
                #remove the character from 0th index
                sub.pop(0)
                i+=1
        return maxLen
                
            

        #Brute force approach
        # #edge cases
        # if(len(s)==1):
        #     return 1
        # i=0
        # maxSub=0
        # sub=[]
        # while(i<len(s)-1):
        #     sub.append(s[i])
        #     for j in range(i+1,len(s)):
        #         if(s[j] not in sub):
        #             sub.append(s[j])
        #         else:
        #             break
        #     maxSub=max(maxSub,len(sub))
        #     sub = [] #make it empty
        #     i+=1
        # return maxSub
