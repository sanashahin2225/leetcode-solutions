from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if set(s) == set(t) and Counter(s) == Counter(t) else False
