# Solution for "1838. Frequency of the Most Frequent Element"
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total, max_length, j = 0, 0, 0

        for i in range(len(nums)):
            total += nums[i]

            while (i - j + 1) * nums[i] - total > k:
                total -= nums[j]
                j += 1

            max_length = max(max_length, i - j + 1)

        return max_length
