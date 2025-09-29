def generateParenthesis( n: int):
        ans = []

        def dfs(current: str, left: int, right: int):
            if left == 0 and right == 0:
                ans.append(current)
                return

            if left > 0:
                dfs(current + "(", left - 1, right)

            if right > left:
                dfs(current + ")", left, right - 1)

        dfs("", n, n)
        return ans