class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        
        # last_pos[j] stores the largest index in word1 such that
        # word2[j:] is a subsequence of word1[last_pos[j]:]
        last_pos = [-1] * (m + 1)
        last_pos[m] = n
        
        # Build suffix matching positions from right to left
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last_pos[j] = i
                j -= 1
        
        ans = []
        changed = False
        j = 0
        
        # Greedily match left-to-right to ensure lexicographically smallest indices
        for i in range(n):
            if j == m:
                break
                
            # Direct match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1
            # Mismatch: check if we can use our single allowed change
            elif not changed and last_pos[j + 1] > i:
                ans.append(i)
                changed = True
                j += 1
                
        return ans if len(ans) == m else []