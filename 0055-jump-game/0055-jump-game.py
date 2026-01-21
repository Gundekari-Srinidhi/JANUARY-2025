class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxInd=0
        for i in range(len(nums)):
            if maxInd<i:
                return False
            maxInd=max(maxInd,i+nums[i])
        return True
        