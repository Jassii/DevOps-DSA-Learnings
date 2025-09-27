class Solution:
	def twoSum(self, arr, target):
		# code here
		
		#Brute force approach
# 		for i in range(0,len(arr)-1):
# 		    for j in range(i+1,len(arr)):
# 		        if(arr[i]+arr[j]==target):
# 		            return True
# 		return False

    #Optimized Approach
        #it will track value of the array with its index
        hash_map = {}
        
        #no pair is there
        if(len(arr)==1):
            return False
        
        for i in range(0,len(arr)):
            second=target-arr[i]
            if(second in hash_map):
                return True
            else:
                hash_map[arr[i]]=i
        return False
