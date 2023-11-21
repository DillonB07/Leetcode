# Solution for "1814. Count Nice Pairs in an Array"

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        rev_diff_freq = {}
        nice_pairs = 0

        for num in nums:
            rev_num = int(str(num)[::-1])
            diff = num - rev_num
            rev_diff_freq[diff] = rev_diff_freq.get(diff, 0) + 1

        for count in rev_diff_freq.values():
            # Calculate the number of pairs that can be formed with 'count' occurrences of a particular difference
            nice_pairs = (nice_pairs + (count * (count - 1) // 2)) % MOD

        return nice_pairs
