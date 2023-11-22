# Solution for "1424. Diagonal Traverse II"
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])

        out = []
        current = 0

        while current in groups:
            out.extend(groups[current])
            current += 1

        return out
