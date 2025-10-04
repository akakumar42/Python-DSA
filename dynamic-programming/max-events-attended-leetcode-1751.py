class Solution(object):
    def maxValue(self, events, k):
        """
        :type events: List[List[int]]
        :type k: int
        :rtype: int
        """
        events.sort()
        n = len(events)
        starts = [e[0] for e in events]
        memo = {}

        def rec(i, k):
            if i == n or k == 0:
                return 0
            if (i, k) in memo:
                return memo[(i, k)]

            # Skip current event
            skip = rec(i + 1, k)

            # Take current event
            next_i = bisect.bisect_right(starts, events[i][1])
            take = events[i][2] + rec(next_i, k - 1)

            memo[(i, k)] = max(skip, take)
            return memo[(i, k)]

        return rec(0, k)