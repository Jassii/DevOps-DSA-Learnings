class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        long_prefix=str()

        for i in range(0,len(first_word)):
            ch = first_word[i]
            for j in range(1,len(strs)):
                new_string=strs[j]
                
                #if the index of the first string crosses the length of any string, then simply return the long_prefix, no need to check for the remaining string
                # if(i>=len(new_string)):
                #     return long_prefix
                # elif(new_string[i]!=ch):
                #     return long_prefix

                #more optimized if block
                if(i==len(new_string) or new_string[i]!=ch):
                    return long_prefix
                           
            #if it reaches here that means, it comes under the prefix
            long_prefix=long_prefix+ch

        return long_prefix
