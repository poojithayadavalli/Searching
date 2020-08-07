"""

Given a sorted array arr[] of size n and a value X, find the k closest elements to X in arr[].

Input:
Firstline indicates integer n
Second consists of elements of array
thirdline indicates integer x and integer k

Output:
print the closest elements in sorted order

Examples:

Input:
13
12 16 22 30 35 39 42 45 48 50 53 55 56
35 4

Output:

30 39 42 45

Expalnation :
The 4 closest elements for 35 are  39 30 42 45.

Input:
5
1 2 3 4 5
4 2

Output:
3 5
"""
def findCrossOver(arr, low, high, x) :
    if (arr[high] <= x): 
        return high 
          
    if (arr[low] > x) : 
        return low
    mid = (low + high) // 2
    if (arr[mid] <= x and arr[mid + 1] > x) : 
        return mid
    
    if(arr[mid] < x) : 
        return findCrossOver(arr, mid + 1, high, x) 
      
    return findCrossOver(arr, low, mid - 1, x) 
 
def printKclosest(arr, x, k, n) :
    
    l = findCrossOver(arr, 0, n - 1, x) 
    r = l + 1 
    count = 0
    if (arr[l] == x) : 
        l -= 1
    res=[]
    while (l >= 0 and r < n and count < k) : 
          
        if (x - arr[l] <=arr[r] - x) : 
            res.append(str(arr[l])) 
            l -= 1
        else : 
            res.append(str(arr[r])) 
            r += 1
        count += 1
    while (count < k and l >= 0) : 
        res.append(str(arr[l]))
        l -= 1
        count += 1
    while (count < k and r < n) :  
        res.append(str(arr[r])) 
        r += 1
        count += 1
    return " ".join(res)
n=int(input())
arr=list(map(int,input().split()))
x,k=map(int,input().split())
print(printKclosest(arr,x,k,n))
