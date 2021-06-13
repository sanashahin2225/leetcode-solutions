class Solution:
    def intToRoman(self, num: int) -> str:
        if num == 0:
            return 0
        
        int_to_roman = {
            1000 : 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        def roman_num(num):
            for r in int_to_roman.keys():
                x, y = divmod(num, r)
                yield int_to_roman[r] * x
                num -= (r * x)
                if num <= 0:
                    break

        return "".join([a for a in roman_num(num)])
