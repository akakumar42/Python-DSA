class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        adj = {num: [] for num in range(n)}

        for f, t, p in flights:
            adj[f].append([t, p])

        heap = [(0, src, 0)]
        visited = {}

        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k:
                continue

            if (node in visited and visited[node] <= stops):
                continue
            visited[node] = stops
            for neighbor, price in adj[node]:
                heapq.heappush(heap, (cost + price, neighbor, stops + 1))

        return -1