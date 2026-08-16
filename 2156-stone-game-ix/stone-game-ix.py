class Solution(object):

    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # Count the frequency of remainders when divided by 3
        cnt = [0] * 3
        for stone in stones:
            cnt[stone % 3] += 1

        # Case 1: Even number of 0-remainder stones
        # 0-remainder stones don't change turn parity, so they can be ignored.
        # Alice needs at least one stone of both 1 and 2 remainders to win.
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0

        # Case 2: Odd number of 0-remainder stones
        # The single effective 0-remainder stone flips the advantage.
        # Alice wins if the count difference between 1-remainder and 2-remainder stones is strictly greater than 2.
        return abs(cnt[1] - cnt[2]) > 2