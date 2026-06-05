class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #first remove space from the left and right
        s=s.strip()

        #then make it into a list separated by space
        res=s.split(" ")

        #return the length of the last word in the list
        return len(res[len(res)-1])
