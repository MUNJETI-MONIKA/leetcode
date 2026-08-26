class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod=10**9+7
        oddcount=0
        evencount=1
        sum=0
        result=0
        for num in arr:
            sum+=num
            if sum%2==0:
                result=(result+oddcount)%mod
                evencount+=1
            else:
                result=(result+evencount)%mod
                oddcount+=1
        return result            