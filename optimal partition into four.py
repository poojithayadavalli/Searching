"""
Given an array of n non-negative integers. Choose three indices i.e. (0 <= index_1 <= index_ 2<= index_3 <= n) from the array 

to make four subsets such that the term sum(0, index_1) – sum(index_1, index_2) + sum(index_2, index_3) – sum(index_3, n) is maximum possible.

Here, two indices say l and r means, the sum(l, r) will be the sum of all numbers of subset on positions from l to r non-inclusive 

(l-th element is not counted, r-th element is counted). 

For example, if arr = {-5, 3, 9, 4}, then sum(0, 1) = -5, sum(0, 2) = -2, sum(1, 4) = 16 and sum(i, i) = 0 for each i from 0 to 4.

For indices l and r holds 0 <= l <= r <= n. Indices in array are numbered from 0.

Input:
First line contains integer n
Second line contains elements of array

Output:
Print the indices that follows given condition

Examples:

Input :
3
-1 2 3
Output :
0 1 3

Explanation:
Here, sum(0, 0) = 0
      sum(0, 1) = -1
      sum(1, 3) = 2 + 3 = 5
      sum(3, 3) = 0
Therefore , sum(0, 0) - sum(0, 1) + sum(1, 3) - sum(3, 3) = 4
which is maximum.

Input :
4
0 0 -1 0

Output :
0 0 0
Here, sum(0, 0) - sum(0, 0) + sum(0, 0) - sum(0, 0) = 0
which is maximum possible.

"""
max = 50009
def findInd(arr, n): 
  
    sum=[0 for i in range(max)] 
    k=0
    for i in range(1,n+1): 
        sum[i] = sum[i-1] + arr[k]; 
        k+=1
       
    ans = -(1e15) 
    index_1 = index_2 = index_3 = -1
    for l in range(n+1): 
        index = 0
        vmin = (1e15) 
        for r in range(l,n+1): 
            if (sum[r] < vmin): 
                vmin = sum[r] 
                index = r
            if (sum[l] + sum[r] - vmin > ans):  
              
                ans = sum[l] + sum[r] - vmin 
                index_1 = l 
                index_2 = index 
                index_3 = r 
    print(index_1,"", index_2,"", index_3)
n=int(input())
arr=list(map(int,input().split()))
findInd(arr,n)
