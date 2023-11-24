# Solution for "1561. Maximum Number of Coins You Can Get"
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0

        piles.sort()
        queue = deque(piles)

        while len(queue) > 0:
            queue.pop()
            ans += queue.pop()
            queue.popleft()

        return ans
