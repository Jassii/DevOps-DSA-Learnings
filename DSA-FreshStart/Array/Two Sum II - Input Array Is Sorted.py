class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        res=[]
        while(l<r):
            if((numbers[l]+numbers[r])==target):
                res.append(l+1)
                res.append(r+1)
                break
            elif((numbers[l]+numbers[r])>target):
                r-=1
            else:
                l+=1
        return res
        
        #Brute force approach
        # res=[0]*2 #result array is of size two (i,j with j is one ahead of i)
        # hmap={}
        # for i in range(0,len(numbers)):
        #     diff=target-numbers[i]
        #     if(diff not in hmap):
        #         hmap[numbers[i]]=i
        #     else:
        #         #add +1 as it is one indexed array of integers
        #         res[0]=hmap[diff]+1
        #         res[1]=i+1
        #         break
        # return res
