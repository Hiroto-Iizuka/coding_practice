import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.top_k_values = nums
        heapify(self.top_k_values)
        while len(self.top_k_values) > self.k:
            heappop(self.top_k_values)

    def add(self, val: int) -> int:
        heappush(self.top_k_values, val)

        if len(self.top_k_values) > self.k:
            heappop(self.top_k_values)

        return self.top_k_values[0]