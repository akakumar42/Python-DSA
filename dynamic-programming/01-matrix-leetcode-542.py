def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n, m = len(mat), len(mat[0])
        dp = [[float('inf')] * m for _ in range(n)]

        # First pass: top-left to bottom-right
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)

        # Second pass: bottom-right to top-left
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if i < n-1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                if j < m-1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)

        return dp