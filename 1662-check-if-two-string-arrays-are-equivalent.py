# Solution for "1662. Check if Two String Arrays are Eqivalent"
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
            return ''.join(word1) == ''.join(word2)
