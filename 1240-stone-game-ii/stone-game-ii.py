class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        
        # Calculate suffix sums so suffix_sum[i] stores the sum of piles[i:]
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}

        def dp(i: int, m: int) -> int:
            # Base case: if remaining piles can all be taken in one move
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            if (i, m) in memo:
                return memo[(i, m)]
            
            # The current player wants to maximize their score.
            # Total stones remaining from index i is suffix_sum[i].
            # Subtracting the maximum score the next player can get gives current player's best score.
            max_stones = 0
            for x in range(1, 2 * m + 1):
                next_m = max(m, x)
                max_stones = max(max_stones, suffix_sum[i] - dp(i + x, next_m))
                
            memo[(i, m)] = max_stones
            return max_stones

        return dp(0, 1)