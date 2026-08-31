class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def num_ways(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        
        same, diff = 0, k

        for i in range(2, n + 1):
            same, diff = diff, (same + diff) * (k - 1)

        return same + diff
    