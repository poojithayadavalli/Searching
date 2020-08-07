"""

Given a sorted array with n integer and a number x, find a pair in array whose sum is closest to x.

Input:
Firstline indicates the integer n and integer x
Secondline contains the elements of sorted array

Output:
print the pair with sum close to x

Examples:

Input:
6 54
10, 22, 28, 29, 30, 40

Output: 
22 30

Explanation:
The sum of pair 22 ,30 is closest to 54 out of sum of all other pairs

Input:
5 15
1 3 4 7 10

Output:
4 10

"""
MAX_VAL = 1000000000
def printClosest(arr, n, x):
    res_l, res_r = 0, 0
    l, r, diff = 0, n-1, MAX_VAL
    while r > l:
        if abs(arr[l] + arr[r] - x) < diff: 
            res_l = l 
            res_r = r 
            diff = abs(arr[l] + arr[r] - x) 
      
        if arr[l] + arr[r] > x:
            r -= 1
        else:
            l += 1
          
    print('{} {}'.format(arr[res_l], arr[res_r]))
n,x=map(int,input().split())
arr=list(map(int,input().split()))
printClosest(arr,n,x)
