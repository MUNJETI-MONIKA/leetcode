class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        has_non_zero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_non_zero = True
                
        if not has_non_zero:
            return 0
        
        return len(nums) if total_xor != 0 else len(nums) - 1