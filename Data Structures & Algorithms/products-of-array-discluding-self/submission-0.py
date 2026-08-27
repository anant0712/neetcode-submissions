class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result=[1]*n

        left_prefix=right_prefix=1

        for i in range(n):
            result[i] = left_prefix
            left_prefix *= nums[i]
        
        for i in range(n-1,-1,-1):
            result[i] *= right_prefix
            right_prefix *= nums[i]
        return result