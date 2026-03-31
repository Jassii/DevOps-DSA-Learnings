nums = [[5,9,1],[2,3,7]]

r = len(nums) #rows
c = len(nums[0]) #columns

#inorder to initialize the 2D matrix
result = [[0]*r for _ in range(0,c)]
print(result)

for i in range(0,r):
    for j in range(0,c):
        result[j][i] = nums[i][j]
    print(result)
print(result)
