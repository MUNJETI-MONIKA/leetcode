class Solution:
    def findMaxLength(self,nums):
        mymap={0:-1}
        sum=0
        longest_subarray=0
        for i in range(len(nums)):
            sum+=-1 if nums[i]==0 else 1
            if sum in mymap:
                longest_subarray=max(longest_subarray,i-mymap[sum])
            else:
                mymap[sum]=i
        return longest_subarray