class Solution:
    def maxSumTwoNoOverlap(self, nums: list[int], firstLen: int, secondLen: int) -> int:
        def maxSum(f: int, s: int) -> int:
            lsum,rsum=sum(nums[:f]),sum(nums[f:f+s])
            best=lsum
            ans=best+rsum
            for i in range(f+s,len(nums)):
                lsum+=nums[i-s]-nums[i-s-f]
                rsum+=nums[i]-nums[i-s]
                best=max(best,lsum);ans=max(ans,best+rsum)
            return ans
        return max(maxSum(firstLen,secondLen),maxSum(secondLen,firstLen))    
