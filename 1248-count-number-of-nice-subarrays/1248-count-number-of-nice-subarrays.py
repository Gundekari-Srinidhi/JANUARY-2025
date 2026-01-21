class Solution:
    def numberOfSubarrays(self, nums: List[int], goal: int) -> int:
        def binary(nums,goal):
            if goal<0:
                return 0
            left,right=0,0
            n=len(nums)
            Sum=0
            count=0
            while right<n:
                Sum+=nums[right]
                while Sum>goal:
                    Sum-=nums[left]
                    left+=1
                count+=right-left+1
                right+=1
            return count
        for i in range(len(nums)):
            nums[i]=nums[i]%2

        return binary(nums,goal)-binary(nums,goal-1)
        
        