class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        #brute force approach
        # pos=[]
        # neg=[]
        # res=[]
        # for i in range(0,len(nums)):
        #     if(nums[i]<0):
        #         neg.append(nums[i])
        #     else:
        #         pos.append(nums[i])
        
        # #result will have first element as positive integer
        # res.append(pos[0])

        #the below logic can be replaced by the formula as well i.e. 2*i and 2*i+1 (for i in range(len(pos))..
        # i=1 #for positive
        # j=0 #for negative
        # k=False
        # while(i<len(pos) or j<len(neg)):
        #     if(k==False):
        #         res.append(neg[j])
        #         j+=1
        #         k=True
        #     else:
        #         res.append(pos[i])
        #         i+=1
        #         k=False
        # return res

        #Optimized Approach
        pos=0 #index for positive integer
        neg=1 #index for negative integer
        res=[0]*len(nums) #list of specific size and initialize with zeros
        for i in range(0,len(nums)):
            if(nums[i]>0):
                res[pos]=nums[i]
                pos+=2 #it will skip the next index for the neg value
            else:
                res[neg]=nums[i]
                neg+=2 #it will skip the nex index for the pos value
        return res 
