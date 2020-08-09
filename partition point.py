"""
Given an array a of size N. The task is to find an index ‘i’ (1 <= i <= N) such that (a[1] ^ … ^ a[i]) + (a[i+1] ^ … ^ a[N]) 

(x^y represents the xor value of x and y) is maximum possible.

Note : Use 1 based indexing

Input:
First line contains integer n
Second line contains elements of array

Output:
print the index at which the sum of xor values is maximum

Examples:

Input :
10
1 4 6 3 8 13 34 2 21 10

Output : 
2

Explanation : The maximum value is 68 at index 2
 
Input : 
9
1 2 3 4 5 6 7 8 9

Output :
8
"""
def ComputePrefixXor(arr, PrefixXor, n): 
    PrefixXor[0] = arr[0]
    for i in range(1, n): 
        PrefixXor[i] = PrefixXor[i - 1] ^ arr[i]

def Xor_Sum(arr, n):
    PrefixXor = [0] * n
    ComputePrefixXor(arr, PrefixXor, n) 
    sum1, index = 0, 0
    for i in range(n):
        if (PrefixXor[i] + (PrefixXor[n - 1] ^PrefixXor[i]) > sum1):  
            sum1 = PrefixXor[i] +(PrefixXor[n - 1] ^ PrefixXor[i])
            index = i
            print(sum1,i)
    return index + 1
n=int(input())
arr=list(map(int,input().split()))
print(Xor_Sum(arr,n))
