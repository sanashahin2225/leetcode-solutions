class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for i in digits:
            string = string + str(i)
        return(','.join(str(int(string)+1).split()))
