class Solution:
    def mySqrt(self, x: int) -> int:
        #Brute force approach
        # closestValue=0
        # for i in range(0,x+1):
        #     value = i*i
        #     if(value==x):
        #         return i
        #     elif(value<x):
        #         closestValue=i
        #     else:
        #         break
        # return closestValue

        #Binary seach approach
        start=0
        end=x
        res=0
        while(start<=end):
            mid=start+(end-start)//2
            square=mid*mid
            if(square==x):
                return mid
            elif(square<x):
                #it can be my result
                res=mid
                start=mid+1
            else:
                end=mid-1
        return res
