class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        memo = {}
        def dfs(x, y1, y2):
            if (x, y1, y2) in memo:
                return memo[(x, y1, y2)]

            if y1 < 0 or y1 >= len(grid[0]) or y2 < 0 or y2 >= len(grid[0]):
                return 0
            
            cherries = grid[x][y1]

            if y1 != y2:
                cherries += grid[x][y2]
            
            if x == len(grid) - 1:
                return cherries
            
            max_cherries = 0
            for next_y1 in [y1 - 1, y1, y1 + 1]:
                for next_y2 in [y2 - 1, y2, y2 + 1]:
                    max_cherries = max(max_cherries, dfs(x + 1, next_y1, next_y2))

            memo[(x, y1, y2)] = cherries + max_cherries
            
            return cherries + max_cherries

        return dfs(0, 0, len(grid[0]) - 1)