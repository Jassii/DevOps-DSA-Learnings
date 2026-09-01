class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #result array 
        res=[]
        for i in range(0,numRows):
            lis=[] #this will store each list
            for j in range(0,i+1):
                if(j==0 or j==i): #if its 0th and last index, then insert1
                    lis.append(1)
                else: #get the last list, and as per j, take sum of j value and j-1 value from prev list
                    prev_list=res[i-1]
                    summ=prev_list[j]+prev_list[j-1] #sum
                    lis.append(summ) #append in the list
            res.append(lis) #insert into the final list
        return res
