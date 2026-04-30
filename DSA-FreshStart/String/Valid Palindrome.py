class Solution:
    def isPalindrome(self, s: str) -> bool:
        #base case
        if(len(s)==0 or len(s)==1):
            return True
        
        #first remove all the non alphanumeric characters
        new_s=""
        for i in range(0,len(s)):
            if((s[i]>='A' and s[i]<='Z') or (s[i]>='a' and s[i]<='z') or (s[i]>='0' and s[i]<='9')):
                new_s+=s[i]
        
       
        #convert new string into lower case
        new_s = new_s.lower()

        l=0
        r=len(new_s)-1
        while(l<r):
            if(new_s[l]!=new_s[r]):
                return False
            l+=1
            r-=1
        return True
