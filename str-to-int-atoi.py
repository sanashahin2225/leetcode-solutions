import re
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        regexlist = ["^[' ']*-?\d+?[0-9]*","^[' ']*[+]?\d+?[0-9]*"]
        lst = []
        for i in regexlist:
            valid = re.search(i,s)
            if valid:
                tmp = int(valid.group(0))
                if tmp > (2 ** 31) - 1:
                    return(2**31 - 1)
                elif tmp < -(2 ** 31):
                    return(-(2 ** 31))
                else:
                    return(tmp)
        return 0
