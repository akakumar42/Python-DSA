class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.memo = {}
        def decode(curr):
            if curr >= len(s):
                return 1
            if curr in self.memo:
                return self.memo[curr]
            count = 0
            if s[curr] <= "9" and s[curr] >= "1":
                count += decode(curr + 1)
            if curr + 1 < len(s) and s[curr:curr + 2] <= "26" and s[curr:curr + 2] >= "10":
                count += decode(curr + 2)

            self.memo[curr] = count            
            return count
        
        return decode(0)
        