def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    return search(0,len(arr)-1,arr,x)

def search(start,end,arr,x):
    ans=len(arr)
    while(start<=end):
        mid = start + (end-start)//2
        if(arr[mid]>x):
            ans=mid
            end=mid-1
        else:
            start=mid+1
    return ans
