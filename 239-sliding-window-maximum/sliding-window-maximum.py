class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq=deque()
        op=[]
        for i in range(len(nums)):
            while dq and nums[i]>nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i-k==dq[0]:
                dq.popleft()
            if i>=k-1:
                op.append(nums[dq[0]])
        return op