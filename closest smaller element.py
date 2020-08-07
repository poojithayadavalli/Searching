"""

Given an array of n integers, find the closest smaller element for every element. If there is no smaller element then print -1

Input:
Firstline indicates size of array n
Secondline contains elements of array

Output:
print closest smaller element for every element in array

Examples:

Input :
6
10 5 11 6 20 12

Output : 
6 -1 10 5 12 11

Explanation:
The closest smaller value for 10 is 6. 5 doest have smaller closest value so -1 .and 11 6 20 11 have closest smaller values as 5 12 11 respectively
Input :
6
10 5 11 10 20 12

Output :
5 -1 10 5 12 11

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
