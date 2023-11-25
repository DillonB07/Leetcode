# Solution for "1685. Sum of Absolute Differences in a Sorted Array"

class Solution:
    # Solution that I made from reading the Editorial
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        result = []

        total_sum = sum(nums)
        left_sum = 0
        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            right_count = n - 1 - i
            left_total = i * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]

            result.append(left_total + right_total)
            left_sum += nums[i]

        return result

    # My Solution with a time complexity of O(N^2)
    def dillonGetSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        return [sum(abs(num - num2) for num2 in nums) for num in nums]
