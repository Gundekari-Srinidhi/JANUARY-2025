class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s=0
        n=len(nums)
        f={0:1}
        prefix_sum=0
        for num in nums:
            prefix_sum+=num
            if prefix_sum-goal in f:
                s+=f[prefix_sum-goal]
            if prefix_sum in f:
                f[prefix_sum]+=1
            else:
                f[prefix_sum]=1
        return s
        