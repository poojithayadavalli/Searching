"""
Given an array arr[] of N positive integers, the task is to count all the contiguous subarrays

where the sum of subarray elements is strictly greater than the sum of remaining elements.

Input:
First line contains integer N
Second line contains elements of array
Output:
Print count of subarrays with sum greater than the remaining element sum
Examples:
Input:
5
1 2 3 4 5

Output: 
6
Explanation:
Subarrays are:
{1, 2, 3, 4} – sum of subarray = 10, sum of remaining elements {5} = 5
{1, 2, 3, 4, 5} – sum of subarray =15, sum of remaining element = 0
{2, 3, 4} – sum of subarray = 9, sum of remaining elements {1, 5} = 6
{2, 3, 4, 5} – sum of subarray = 14, sum of remaining elements {1} = 1
{3, 4, 5} – sum of subarray = 12, sum of remaining elements {1, 2} = 3
{4, 5} – sum of subarray = 9, sum of remaining elements {1, 2, 3} = 6

Input:
4
10 9 12 6

Output: 5

Explanation:
Sub arrays are :
{10, 9} – sum of subarray = 19, sum of remaining elements {12, 6} = 18
{10, 9, 12} – sum of subarray = 31, sum of remaining elements {6} = 6
{10, 9, 12, 6} – sum of subarray = 37, sum of remaining elements = 0
{9, 12} – sum of subarray = 21, sum of remaining elements {10, 6} = 16
{9, 12, 6} – sum of subarray =27, sum of remaining element {10} = 10
"""
def Count(arr, n) :  
  
    total_sum = 0  
    count = 0
    for i in range(n) : 
        total_sum += arr[i]
    for i in range(n-1) : 
        subarray_sum = 0
        for j in range(i, n) :  
            subarray_sum += arr[j] 
            remaining_sum = total_sum - subarray_sum 
            if (subarray_sum > remaining_sum) : 
                count += 1 
          
    return count
n= int(input())
arr=list(map(int,input().split()))
print(Count(arr,n))

