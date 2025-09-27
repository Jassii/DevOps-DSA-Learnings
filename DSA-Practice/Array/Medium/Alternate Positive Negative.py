#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        
        pos=[]
        neg=[]
        for i in range(0,len(arr)):
            if(arr[i]>=0):
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        
        
        p=len(pos)
        n=len(neg)
        
        #count of positive and negative is same
        if(p==n):
            for i in range(0,p):
                arr[i*2]=pos[i]
                arr[i*2+1]=neg[i]
            return arr
        #count of positive numbers is greater than negative
        elif(p>n):
            for i in range(0,n):
                arr[i*2]=pos[i]
                arr[i*2+1]=neg[i]
            
            index=n*2
            #remaning element of pos array list
            for i in range(n,p):
                arr[index]=pos[i]
                index+=1
            return arr
        #count of negative numbers is greater than positive
        else:
            for i in range(0,p):
                arr[i*2]=pos[i]
                arr[i*2+1]=neg[i]
            
            index=p*2
            #remaining element of neg array list
            for i in range(p,n):
                arr[index]=neg[i]
                index+=1
            return arr
            
        
        
        
        #brute force approach
        # neg = []
        # pos = []
        # for i in range(0,len(arr)):
        #     if(arr[i]>=0):
        #         pos.append(arr[i])
        #     else:
        #         neg.append(arr[i])
        
        # #now i have both positive and negative integer arrays.
        # result=[]
        # p=len(pos)
        # n=len(neg)
        
        # i=0 #index for positive array
        # j=0 #index for negative array
        
        # k=0 #just to decide which element should be picked
        
        # while(i<p and j<n):
        #     if(k%2==0): #for positive
        #         result.append(pos[i])
        #         i+=1
        #     else: #for negative
        #         result.append(neg[j])
        #         j+=1
        #     k+=1
        
        # #for the remaining element in any one of the array (pos and neg)
        # while(i<p):
        #     result.append(pos[i])
        #     i+=1
        # while(j<n):
        #     result.append(neg[j])
        #     j+=1
            
        # for i in range(0,len(result)):
        #     arr[i]=result[i]
        
        # return arr
