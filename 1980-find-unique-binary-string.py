# Solution for "1980. Find Unique Binary String"
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        if nums[0] == "0": return "1"
        elif nums[0] == "1": return "0"
        for i in range (n**2):
            s = format(i, '0' + str(n) + 'b')
            if s not in nums:
                return s
