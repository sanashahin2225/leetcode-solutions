class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        if len(s) == 1:
            return False
        else:
            stack = []
            for i in s:
                if i in valid_pair.keys():
                    stack.append(i)
                else:
                    if len(stack) != 0:
                        temp = stack.pop(-1)
                        if valid_pair[temp] != i:
                            return False
                    else:
                        return False
            if len(stack) != 0:
                return False
            return True
                        
