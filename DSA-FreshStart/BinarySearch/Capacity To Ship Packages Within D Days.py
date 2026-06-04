class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #minimum capacity will the max weight
        minC=max(weights)

        #max capacity will be the sum of all weights
        maxC=sum(weights)

        left=minC
        right=maxC

        #result can be the sum of weights
        res=maxC
        while(left<=right):
            midC=left+(right-left)//2
            temp=midC

            #calculate how many ships/days it will require
            ships=1
            for i in range(0,len(weights)):
                #first check if the capacity can go less than 0, then increase the ships
                if(temp-weights[i]<0):
                    ships+=1
                    temp=midC
                temp=temp-weights[i]
            
            #when number of ships/days calculated, then check if it is less than equal to days
            if(ships<=days):
                res=min(res,midC) #it can be the minimum weight capacity
                right=midC-1
            else:
                left=midC+1
        return res
