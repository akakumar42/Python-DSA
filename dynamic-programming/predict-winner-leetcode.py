class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        self.memo = {}

        def dfs(i, j):
            key = (i, j)
            if key in self.memo:
                return self.memo[key]
            if i == j:
                return nums[i]
            pick_left = nums[i] - dfs(i + 1, j)
            pick_right = nums[j] - dfs(i, j - 1)

            self.memo[key] = max(pick_left, pick_right)
            return max(pick_left, pick_right)
            

        return dfs(0, n - 1) >= 0