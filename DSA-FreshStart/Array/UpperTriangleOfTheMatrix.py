nums = [[5,10,8],[7,6,3],[2,1,9]]

r = len(nums) #rows
c = len(nums[0]) #columns

for i in range(0,r):
    #first lets give space
    for j in range(0,i):
        print("*",end=" ") #without changing the line
    
    #then we will print the array values
    for j in range(i,c):
        print(nums[i][j],end=" ")  #without changing the line
    print()
