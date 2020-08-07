"""
Given an array of n integers, find the nearest smaller number for every element such that the smaller element is on left side.

Input:
Firstline indicates integer n
Second line contains the elements of array

Output:
print the closest element for each element in its left side

Examples:

Input:
6
1 6 4 10 2 5

Output:
-1 1  1  6  1  4  

Explanation:
First element ('1') has no element on left side. For 6, 
there is only one smaller element on left side '1'. 
For 10, there are three smaller elements on left side (1,
6 and 4), nearest among the three elements is 6.

Input:
5
1 3 0 2 5
Output:
-1 1 -1 1 3 

"""
def closestSmall(arr,n):
    l=[]
    t=set()
    for i in arr:
        t.add(i)
    t=list(t)
    for i in arr:
        s=t.index(i)-1
        if s==-1:
            l.append(-1)
        else:
            l.append(t[s])
    return l
n=int(input())
arr=list(map(int,input().split()))
print(*closestSmall(arr,n))
