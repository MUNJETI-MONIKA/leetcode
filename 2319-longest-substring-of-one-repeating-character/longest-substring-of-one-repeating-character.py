class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        s_list = list(s)
        
        # Segment tree nodes store:
        # (max_len, pref_len, suff_len, left_char, right_char, length_of_segment)
        tree = [None] * (4 * n)
        
        def merge(left, right):
            l_max, l_pref, l_suff, l_left_char, l_right_char, l_len = left
            r_max, r_pref, r_suff, r_left_char, r_right_char, r_len = right
            
            # Base merged length and characters
            merged_len = l_len + r_len
            merged_left_char = l_left_char
            merged_right_char = r_right_char
            
            # Base prefix and suffix
            merged_pref = l_pref
            merged_suff = r_suff
            
            # Base maximum
            merged_max = max(l_max, r_max)
            
            # Check if middle characters match to merge prefix/suffix across boundary
            if l_right_char == r_left_char:
                merged_max = max(merged_max, l_suff + r_pref)
                
                if l_pref == l_len:
                    merged_pref = l_len + r_pref
                if r_suff == r_len:
                    merged_suff = r_len + l_suff
                    
            return (merged_max, merged_pref, merged_suff, merged_left_char, merged_right_char, merged_len)

        def build(node, start, end):
            if start == end:
                c = s_list[start]
                tree[node] = (1, 1, 1, c, c, 1)
                return
            
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx, ch):
            if start == end:
                tree[node] = (1, 1, 1, ch, ch, 1)
                return
            
            mid = (start + end) // 2
            if idx <= mid:
                update(2 * node, start, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, end, idx, ch)
                
            tree[node] = merge(tree[2 * node], tree[2 * node + 1])

        build(1, 0, n - 1)
        
        ans = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            ch = queryCharacters[i]
            
            if s_list[idx] != ch:
                s_list[idx] = ch
                update(1, 0, n - 1, idx, ch)
                
            # The root node holds the overall max length for s[0...n-1]
            ans.append(tree[1][0])
            
        return ans