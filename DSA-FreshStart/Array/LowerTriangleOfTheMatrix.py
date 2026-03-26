nums = [[5,10,8],[7,6,3],[2,1,9]]

r = len(nums) #rows
c = len(nums[0]) #columns

#one way (simpler)
# for i in range(0,r):
#     for j in range(0,c):
#         if(i>=j):
#             print(nums[i][j],end=" ")
#         else:
#             print("*",end=" ")
#     print()

#another way to do this question
for i in range(0,r):
    for j in range(0,i+1):
        print(nums[i][j],end=" ")
    for j in range(i+1,c):
        print("*",end=" ")
    print()
