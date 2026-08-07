class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        # Step 1: Prime factorize t into 2, 3, 5, 7.
        # If t has any prime factor > 7, it's impossible (digits are 1-9).
        temp = t
        cnt = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in (2, 3, 5, 7):
            while temp % p == 0:
                cnt[p] += 1
                temp //= p
        if temp > 1:
            return "-1"

        n = len(num)

        # Helper function to find minimum digits required to satisfy prime factor counts
        def get_min_digits(c2, c3, c5, c7):
            c2 = max(0, c2)
            c3 = max(0, c3)
            c5 = max(0, c5)
            c7 = max(0, c7)
            
            # Combine prime factors into highest possible digits (9, 8, 6, 4, 2, 3) greedily
            d9 = c3 // 2
            c3 %= 2
            
            d8 = c2 // 3
            c2 %= 3
            
            d6 = 0
            if c2 > 0 and c3 > 0:
                d6 = 1
                c2 -= 1
                c3 -= 1
                
            d4 = c2 // 2
            c2 %= 2
            
            d2 = c2
            d3 = c3
            d5 = c5
            d7 = c7
            
            res = []
            res.extend(['2'] * d2)
            res.extend(['3'] * d3)
            res.extend(['4'] * d4)
            res.extend(['5'] * d5)
            res.extend(['6'] * d6)
            res.extend(['7'] * d7)
            res.extend(['8'] * d8)
            res.extend(['9'] * d9)
            res.sort()
            return "".join(res)

        # Find prefix product factor requirements for num
        pref_c = [{2: 0, 3: 0, 5: 0, 7: 0} for _ in range(n + 1)]
        first_zero = -1

        for i, ch in enumerate(num):
            d = int(ch)
            if d == 0:
                first_zero = i
                break
            
            # Copy previous counts
            for p in (2, 3, 5, 7):
                pref_c[i + 1][p] = pref_c[i][p]
                
            temp_d = d
            for p in (2, 3, 5, 7):
                while temp_d % p == 0:
                    pref_c[i + 1][p] += 1
                    temp_d //= p

        # Check if the original num is valid (no zero and product divisible by t)
        if first_zero == -1:
            if all(pref_c[n][p] >= cnt[p] for p in (2, 3, 5, 7)):
                return num

        # Find the longest matching prefix i in num, then place digit > num[i]
        limit = first_zero if first_zero != -1 else n - 1

        for i in range(limit, -1, -1):
            start_d = int(num[i]) + 1
            
            for d in range(start_d, 10):
                # Calculate remaining prime factors needed
                cur_c = {p: pref_c[i][p] for p in (2, 3, 5, 7)}
                temp_d = d
                for p in (2, 3, 5, 7):
                    while temp_d % p == 0:
                        cur_c[p] += 1
                        temp_d //= p
                
                rem_c2 = cnt[2] - cur_c[2]
                rem_c3 = cnt[3] - cur_c[3]
                rem_c5 = cnt[5] - cur_c[5]
                rem_c7 = cnt[7] - cur_c[7]
                
                min_suffix = get_min_digits(rem_c2, rem_c3, rem_c5, rem_c7)
                rem_len = (n - 1) - i
                
                if len(min_suffix) <= rem_len:
                    # Pad with '1's to match length
                    ones = '1' * (rem_len - len(min_suffix))
                    return num[:i] + str(d) + ones + min_suffix

        # If no prefix match works, generate a number with length n + 1
        min_str = get_min_digits(cnt[2], cnt[3], cnt[5], cnt[7])
        ones = '1' * ((n + 1) - len(min_str))
        return ones + min_str