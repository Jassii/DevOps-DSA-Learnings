class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #brute force approach -> O(n^2)
        # profit=0
        # for i in range(0,len(prices)-1):
        #     cp=prices[i] #at this price stock is bought
        #     #now need to find value greater than cp, hence to have a profit
        #     for j in range(i+1,len(prices)):
        #         if(prices[j]>cp):
        #             profit=max(profit,prices[j]-cp)  
        # return profit


        #Optimized Approach - Only maintaining minimum price. - O(n)
        profit=0
        min_price=prices[0]
        for i in range(1,len(prices)):
            #if profit is there
            if(prices[i]>min_price):
                profit=max(profit,prices[i]-min_price)
            else:
                min_price=min(min_price,prices[i]) 
        return profit
