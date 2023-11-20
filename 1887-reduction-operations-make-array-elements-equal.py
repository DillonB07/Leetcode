# Solution for "1887. Reduction Operations to Make the Array Elements Equal"
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        up = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                up += 1
            ans += up

        return ans
