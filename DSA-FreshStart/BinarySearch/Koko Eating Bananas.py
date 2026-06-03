import math
import sys
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minBanana=sys.maxsize-1

        #max banana koko can eat in one hour
        maxBanana = max(piles)

        #suppose koko can eat minimum one banana
        start=1
        end=maxBanana
        while(start<=end):
            mid=start+(end-start)//2 #this much banana koko eats in an hour
            #with mid banana's, how many hours will it take for koko to eat while piles
            tot_hours=0
            for i in range(0,len(piles)):
                value=math.ceil(piles[i]/mid) #upper value
                tot_hours+=value
            #if total hours by koko is less than equal to h, mid can be the banana count per hour
            if(tot_hours<=h):
                minBanana=min(minBanana,mid)
                end=mid-1
            else:
                start=mid+1
        #at last return the minimum banana koko can eat full piles in less than equal to h hours
        return minBanana
