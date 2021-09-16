class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char for char in s if char.isalnum())
        if new_string.lower() == new_string.lower()[::-1]:
            return True
        else:
            return False
