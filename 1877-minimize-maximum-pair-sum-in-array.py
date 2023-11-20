# Solution for "1877. Minimize Maximum Pair Sum in Array"
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        highest = 0
        for num in range(int(len(nums)/2)):
            highest = max(highest, nums[num] + nums[len(nums) - 1 - num])
        return highest
