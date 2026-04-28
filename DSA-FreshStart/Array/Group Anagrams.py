class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #Brute Force Approach
        # res=[]
        # sorted_strs=[]

        # #traverse the strs list and sort each string and store in a new list
        # for i in range(0,len(strs)):
        #     s = strs[i]
        #     sorted_strs.append(''.join(sorted(s)))

        # #now sorted_strs will have the sorted strings

        # #taking one more array which will track visited in the strs/sorted_strs
        # visited = [False]*len(strs)

        # inside_list=[]
        # for i in range(0,len(sorted_strs)):
        #     if(visited[i]==True):
        #         continue
        #     inside_list.append(strs[i])
        #     for j in range(i+1,len(sorted_strs)):
        #         if(sorted_strs[j]==sorted_strs[i] and visited[j]==False):
        #             inside_list.append(strs[j])
        #             visited[j]=True
        #     #inside list is created, now add that list in the result list
        #     res.append(inside_list)
        #     inside_list = [] #make it empty
        
        # return res


        #Optimized Way using HashMap (Categorize by Sorting)
        hmap=defaultdict(list)
        for i in range(0,len(strs)):
            sorted_word = ''.join(sorted(strs[i]))
            origal_list = []
            if(sorted_word not in hmap):
                hmap[sorted_word].append(strs[i])
            else:
                value = hmap[sorted_word]
                print(value)
                value.append(strs[i])
                hmap[sorted_word] = value

        res=[]
        for key,value in hmap.items():
            res.append(value)
        
        return res
