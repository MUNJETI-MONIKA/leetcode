class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Find the longest sequential prefix sum starting at index 0
        prefix_sum = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1

        # Step 2: Convert nums to a set for O(1) lookup speed
        num_set = set(nums)

        # Step 3: Find the smallest integer >= prefix_sum that is missing from nums
        ans = prefix_sum
        while ans in num_set:
            ans += 1

        return ans