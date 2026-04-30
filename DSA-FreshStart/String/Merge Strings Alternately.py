class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        #optimized approach
        i=0
        j=0
        res=[]
        while(i<len(word1) and j<len(word2)):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        
        #one of the string has been fully traversed
        res.append(word1[i:])
        res.append(word2[j:])
        
        #at last convert the list into string and return it
        return "".join(res)


        #Brute Force Approach
        # n1=len(word1)
        # n2=len(word2)

        # #edge case
        # if(n1==0):
        #     return word2
        # elif(n2==0):
        #     return word1

        # #now we are sure that each word length is greater than equal to 1
        # res=""
        # #as the merge string starts with word1
        # res+=word1[0]

        # i=1 #index of word1
        # j=0 #index of word2
        # alt=True
        # while(i<n1):
        #     if(alt==True):
        #         if(j<n2):
        #             res+=word2[j]
        #             j+=1
        #             alt=False
        #         else:
        #             alt=False
        #     else:
        #         res+=word1[i]
        #         i+=1
        #         alt=True
        

        # #it will come out once it reaches the end of the word1 string
        # while(j<n2):
        #     res+=word2[j]
        #     j+=1
        
        # return res
