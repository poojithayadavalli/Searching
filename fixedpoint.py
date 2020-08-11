"""
Given an array of n distinct integers sorted in ascending order, write a function that returns a Fixed Point in the array,

if there is any Fixed Point present in array, else returns -1. 

Fixed Point in an array is an index i such that arr[i] is equal to i. Note that integers in array can be negative.

Input:
Firstline indicates the integer n
Secondline contains the elements of array

Output:
print the fixed point

Examples:

  Input:
  5
  -10 -5 0 3 7
  
  Output: 
  3
  
  Expalnation :
  Here Array[3]=3 hence 3 is fixed point

  Input:
  5
  0 2 5 8 17
  
  Output: 0 


  Input:
  6
  -10 -5 3 7 9
  
  Output:
  -1
  
  """
def fp(arr, n):
  for i in range(n):
    if arr[i] is i:
      return i
  return -1
n=int(input())
arr=list(map(int,input().split()))
print(fp(arr,n))
