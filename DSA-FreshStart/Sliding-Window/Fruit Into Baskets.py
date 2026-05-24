class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
      #sliding window approach
        l=0
        r=0
        maxF=0
        mapSize=2
        fruits_count=dict()
        while(r<len(fruits)):
            fruit=fruits[r]
            if(fruit not in fruits_count):
                if(mapSize>0):
                    fruits_count[fruit]=1
                    mapSize-=1
                    r+=1
                else:
                    #now you cannot put the new fruit, so now cancluate the maxF
                    count=0
                    for key,value in fruits_count.items():
                        count+=value
                    maxF=max(maxF,count)
                    #now its that state where one basket needs to be empty, which ever key's value becomes zero first, that will
                    #be removed
                    while(l<r):
                        fruits_count[fruits[l]] = fruits_count[fruits[l]]-1
                        if(fruits_count[fruits[l]]==0):
                            break
                        l+=1
                    #now value at l is 0, now I have to revove the key at l position from the map
                    fruits_count.pop(fruits[l])
                    l+=1
                    mapSize=1
            else:
                fruits_count[fruit]=fruits_count.get(fruit)+1
                r+=1
        
        #now calculate the max number of Fruits picked
        count=0
        for key,value in fruits_count.items():
            count+=value
        maxF=max(maxF,count)
        return maxF
