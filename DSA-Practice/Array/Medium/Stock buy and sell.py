import sys
class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
        # code here
        # maxP=0
        # total=0
        # mini=sys.maxsize
        # for i in range(0,len(arr)):
        #     if(arr[i]<mini):
        #         mini=arr[i]
        #         total+=maxP
        #     maxP = max(maxP,arr[i]-mini)
        
        # #at last when the loop is complete
        # total += maxP
        
        # return total

        #total profit
        profit=0
        for i in range(1,len(arr)):
            if(arr[i]>arr[i-1]):
                profit += arr[i]-arr[i-1]   #track the summation of the profit
        return profit
