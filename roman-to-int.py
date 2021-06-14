class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_TO_INT = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL':  40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }
        
        res = 0
        i=0
        if len(s) == 1:
            return ROMAN_TO_INT[s]
        while i < len(s)-1:
            if ROMAN_TO_INT[s[i]] >= ROMAN_TO_INT[s[i+1]]:
                res += ROMAN_TO_INT[s[i]]
                i += 1
            else:
                res += ROMAN_TO_INT[s[i+1]] - ROMAN_TO_INT[s[i]]
                i += 2
            
            if i == len(s)-1:
                res += ROMAN_TO_INT[s[i]]
        return res
