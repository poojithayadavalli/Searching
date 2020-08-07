"""

Given, an array of size n. Find an element which divides the array in two sub-arrays with equal sum.

Print -1 if no such index exists.

Input:
Firstline indicates the integer n
Secondline consists of elements of array

Output:
print the index that divides array into two subarrays with equal sum

Examples:

Input :
4
1 4 2 5
Output : 
2

Explanation : If 2 is the partition, subarrays are : {1, 4} and {5}

Input : 
6
2 3 4 1 4 5
Output :
1
Explanation : If 1 is the partition, 
 Subarrays are : {2, 3, 4} and {4, 5}
 
 """
def findElement(arr, size) : 
  
    right_sum, left_sum = 0, 0
    for i in range(1, size) : 
        right_sum += arr[i]
    i, j = 0, 1 
    while j < size : 
        right_sum -= arr[j] 
        left_sum += arr[i] 
  
        if left_sum == right_sum : 
            return arr[i + 1]
        j += 1
        i += 1
  
    return -1
n=int(input())
arr=list(map(int,input().split()))
print(findElement(arr,n))


