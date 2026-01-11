import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_ascending = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.top_k_ascending) < self.k:
            heapq.heappush(self.top_k_ascending, val)
        else:
            heapq.heappushpop(self.top_k_ascending, val)
        return self.top_k_ascending[0]