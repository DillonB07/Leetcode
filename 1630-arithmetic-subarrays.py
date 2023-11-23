# Solution for "1630. Arithmetic Subarrays"
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i]+1]
            ans.append(self._check(arr))
        return ans
    
    def _check(self, arr:list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for j in range(2, len(arr)):
            if arr[j] - arr[j-1] != diff:
                return False
        return True
