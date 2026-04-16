class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Brute force approach
        #if length of the string is different, then t is not an anagram of s
        if(len(s)!=len(t)):
            return False
        
        map_s,map_t=dict(),dict()
        for c in s:
            map_s[c]= 1 + map_s.get(c,1)
        
        for c in t:
            map_t[c]=1+map_t.get(c,1)
        
        #now we can compare two maps
        for key,value in map_s.items():
            if(key not in map_t):
                return False
            if(map_t[key]!=value):
                return False
        return True



        #another approach, use the Counter data structure of Python
        # return Counter(s)==Counter(t)

        #another approach using sorting
        # st = ''.join(sorted(s))
        # tt = ''.join(sorted(t))
        # return st==tt
