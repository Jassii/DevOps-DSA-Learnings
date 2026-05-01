class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while(l<r):
            if(s[l]!=s[r]):
                #now need to check if character to remove and check if its makes a palindrome
                
                #now trying to remove l place character from the string s
                new_string_l = s[0:l]+s[l+1:]
                new_string_l_rev = new_string_l[::-1]
                if(new_string_l == new_string_l_rev):
                    return True
                
                #now trying to remove r place character from the string s
                new_string_r = s[0:r]+s[r+1:]
                new_string_r_rev = new_string_r[::-1]
                if(new_string_r == new_string_r_rev):
                    return True
                
                #if removal did not make it palindrome, then return False (as only one atmost character we can remove)
                return False

            else:
                l+=1
                r-=1

        return True
