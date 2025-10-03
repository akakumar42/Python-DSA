class Solution(object):
    def countPalindromicSubsequences(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        MOD = 10**9 + 7
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    left = i + 1
                    right = j - 1
                    while left <= right and s[left] != s[i]:
                        left += 1
                    while left <= right and s[right] != s[i]:
                        right -= 1
                    if left > right:
                        dp[i][j] = dp[i+1][j-1] * 2 + 2
                    elif left == right:
                        dp[i][j] = dp[i+1][j-1] * 2 + 1
                    else:
                        dp[i][j] = dp[i+1][j-1] * 2 - dp[left+1][right-1]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
                dp[i][j] %= MOD
        return dp[0][n-1]