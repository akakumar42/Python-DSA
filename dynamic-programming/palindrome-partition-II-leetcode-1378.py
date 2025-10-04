class Solution(object):
    def palindromePartition(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def findChanges(s):
            start = 0
            end = len(s) - 1
            if start == end:
                return 0
            count = 0
            while start < end:
                if s[start] != s[end]:
                    count += 1
                start += 1
                end -= 1
            return count

        n = len(s)
        
        
        changes = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    changes[i][j] = changes[i + 1][j - 1] if i + 1 <= j - 1 else 0
                else:
                    changes[i][j] = (changes[i + 1][j - 1] if i + 1 <= j - 1 else 0) + 1

        # Initialize DP table
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0 

        for i in range(1, n + 1):
            dp[i][1] = changes[0][i - 1] 

        for i in range(1, n + 1):
            for j in range(2, k + 1):
                for m in range(j - 1, i):
                    dp[i][j] = min(dp[i][j], dp[m][j - 1] + changes[m][i - 1])

        return dp[n][k]