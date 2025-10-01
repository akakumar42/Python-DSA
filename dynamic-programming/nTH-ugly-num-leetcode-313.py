def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        seen = {1}
        heap = [1]
        
        for _ in range(n):   
            ugly = heapq.heappop(heap)
            for p in primes:
                new_num = ugly * p
                if new_num not in seen:
                    seen.add(new_num)
                    heapq.heappush(heap, new_num)
        
        return ugly