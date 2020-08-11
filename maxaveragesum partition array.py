"""

Given an array, we partition a row of numbers A into at most K adjacent (non-empty) groups, then the score is the sum of the average of each group.

What is the maximum score that can be scored?

Examples:

Input : 
5 3
9 1 2 3 9

Output : 
20

Explanation : We can partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9]. That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.

Input :
7 4
1 2 3 4 5 6 7

Output :
20
Explanation : We can partition A into [1, 2, 3, 4], [5], [6], [7]. The answer is 2.5 + 5 + 6 + 7 = 20.5

"""
def largeSumAvg(A, K): 
  
    n = len(A)
    pre_sum = [0] * (n + 1) 
    pre_sum[0] = 0 
    for i in range(n): 
        pre_sum[i + 1] = pre_sum[i] + A[i] 
    dp = [0] * n 
    sum = 0
    for i in range(n): 
        dp[i] = (pre_sum[n] - pre_sum[i]) / (n - i) 
      
    for k in range(K - 1): 
        for i in range(n): 
            for j in range(i + 1, n):  
                dp[i] = max(dp[i], (pre_sum[j] - pre_sum[i]) / (j - i) + dp[j]) 
      
    return int(dp[0])

n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(largeSumAvg(arr,k))
