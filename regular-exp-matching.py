import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tmp = re.fullmatch(p,s)
        if tmp:
            return True
        else:
            return False
