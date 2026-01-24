class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def func(r,c,dp):
            if(r == 0 and c == 0):
                return 1 
            if(r<0 or c<0):
                return 0
            if(dp[r][c]!=-1):
                return dp[r][c] 
            dp[r][c] = func(r-1,c,dp)+func(r,c-1,dp)
            return dp[r][c] 
        dp = []
        for i in range(m):
            lst = [-1]*n 
            dp.append(lst)
        return func(m-1,n-1,dp)