class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        if dividend == 0:
            return 0
        if divisor > 0 and dividend > 0:
            while dividend >= divisor:
                dividend = dividend - divisor
                if dividend >= 0:
                    quotient += 1
            return quotient
        elif divisor < 0 and dividend > 0:
            while dividend >= abs(divisor):
                dividend = dividend - abs(divisor)
                if dividend >= 0:
                    quotient += 1
            return -quotient
        elif divisor > 0 and dividend < 0:
            while abs(dividend) >= divisor:
                dividend = abs(dividend) - divisor
                if abs(dividend) >= 0:
                    quotient += 1
            return -quotient
        elif divisor < 0 and dividend < 0:
            new_div = abs(divisor)
            new_dividend = abs(dividend)
            while new_dividend >= new_div:
                new_dividend = new_dividend - new_div
                if new_dividend >= 0:
                    quotient += 1
            return quotient
        else:
            return 1
