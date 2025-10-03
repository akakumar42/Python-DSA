class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    min_turn = float('inf')
                    for k in range(i, j):
                        min_turn = min(min_turn, dp[i][k] + dp[k + 1][j])
                    dp[i][j] = min_turn
            
        return dp[0][n - 1]