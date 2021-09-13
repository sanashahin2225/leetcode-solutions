class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_str = s.strip()
        sp = new_str.split()
        return len(sp[-1])
