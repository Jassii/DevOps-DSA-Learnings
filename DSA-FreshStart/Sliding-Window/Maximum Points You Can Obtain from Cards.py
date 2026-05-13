class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #window is of size k
        maxSum=0
        summ=0
        leftSum=0
        rightSum=0

        #take out the left sum
        i=0
        while(i<k):
            leftSum+=cardPoints[i]
            i+=1
        
        summ = leftSum + rightSum
        maxSum = max(maxSum,summ)

        # i=0
        j=k-1
        r=len(cardPoints)-1
        #now will remove one element from the left and add one element from the right
        while(j>=0):
            leftSum-=cardPoints[j]
            j-=1
            rightSum+=cardPoints[r]
            summ = leftSum+rightSum
            maxSum=max(maxSum,summ)
            r-=1

        #j will fail the condition
        return maxSum
