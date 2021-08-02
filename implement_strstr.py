import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        elif len(haystack) == 0 and len(needle) != 0:
            return -1
        elif len(haystack) != 0 and len(needle) == 0:
            return 0
        else:
            temp = re.search(needle,haystack)
            if temp != None:
                return temp.start()
            else:
                return -1
